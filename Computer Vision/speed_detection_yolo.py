from ultralytics import YOLO
import cv2 
import numpy as np
import supervision as sv
from collections import defaultdict, deque


model = YOLO("yolov8m.pt")
cap = cv2.VideoCapture("marina.mp4")

class ViewTransformer:
    """
    Class representing a perspective transformation.

    Attributes:
        source (np.ndarray): Source points for the transformation.
        target (np.ndarray): Target points for the transformation.
        m (np.ndarray): Perspective transformation matrix.
    """
    def __init__(self, source: np.ndarray, target: np.ndarray):
        """
        Initialize the ViewTransformer.

        Args:
            source (np.ndarray): Source points for the transformation.
            target (np.ndarray): Target points for the transformation.
        """
        source = source.astype(np.float32)
        target = target.astype(np.float32)
        self.m = cv2.getPerspectiveTransform(source, target)

    def transform_points(self, points:np.ndarray ) ->np.ndarray:
        """
        Transform points using the perspective transformation.

        Args:
            points (np.ndarray): Points to transform.

        Returns:
            np.ndarray: Transformed points.
        """
        reshaped_points = points.reshape(-1,1,2).astype(np.float32)
        transformed_points = cv2.perspectiveTransform(reshaped_points, self.m)
        return transformed_points.reshape(-1,2)

    
polygonZone = np.array([
[227, 237],[469, 183],[596, 232],[314, 301]
])
target_with = 17.3
target_height = 10.5


target = np.array([
    [0,0],
    [target_with -1, 0],
    [target_with-1, target_height-1],
    [0, target_height-1],
])

video_info = sv.VideoInfo.from_video_path("traffic_marina_segon.mp4")
byte_track = sv.ByteTrack(frame_rate=video_info.fps)
polygon_zone = sv.PolygonZone(polygonZone, frame_resolution_wh= video_info.resolution_wh)

# Initialize annotators and transformers
box_annotator = sv.BoundingBoxAnnotator(thickness=1)
label_annotator = sv.LabelAnnotator(text_scale= 0.4, text_thickness= 1)
view_transformed = ViewTransformer(source= polygonZone, target= target)

coordinates = defaultdict(lambda: deque(maxlen= video_info.fps))
warning_message = "WARNING:SPEEDING"

while True: 
  
    _, frame = cap.read()
    result = model(frame)[0]

    detections = sv.Detections.from_ultralytics(result)
    detections = detections[polygon_zone.trigger(detections)]
    detections = byte_track.update_with_detections(detections=detections)
    points = detections.get_anchors_coordinates(anchor= sv.Position.BOTTOM_CENTER)
    
    if points.any():  # Check if points is not empty
        points = view_transformed.transform_points(points=points).astype(int)

    labels_list = []
    if detections.tracker_id is not None and points is not None:
        for tracker_id, [_,y] in zip(detections.tracker_id, points):
            coordinates[tracker_id].append(y)
            if len(coordinates[tracker_id])< video_info.fps / 2:
                labels_list.append(f"#{tracker_id}")
            else:
                coordinate_start = coordinates[tracker_id][-1]
                coordinate_end =coordinates[tracker_id][0]
                distance = abs(coordinate_start - coordinate_end)
                time = len(coordinates[tracker_id]) / video_info.fps
                speed = distance / time * 3.6
                
                if speed > 31:
                    labels_list.append(f"#{tracker_id} {int(speed)} km/h {warning_message}")
                else:
                    labels_list.append(f"#{tracker_id} {int(speed)} km/h")
    
    frame_ = frame.copy()
    frame_ = box_annotator.annotate(
        scene = frame_, detections= detections)
    frame_ = label_annotator.annotate(
        scene = frame_, detections= detections, labels=labels_list)
    frame_ = sv.draw_polygon(frame_, polygon=polygonZone, color = sv.Color.red(), thickness=1)


    cv2.imshow("Frame", frame_) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
