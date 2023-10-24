resource "aws_s3_bucket" "static" {
  bucket = "learningbucketforuni"

}
resource "aws_s3_bucket_website_configuration" "static_config" {
  bucket = aws_s3_bucket.static.id

  index_document {
    suffix = "home.html"
  }
  }
resource "aws_s3_bucket_ownership_controls" "static_ownership" {
  bucket = aws_s3_bucket.static.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}
data "aws_iam_policy_document" "allow_access" {
  policy_id = "PolicyForCloudFrontPrivateContent"
statement {
  sid = "AllowCloudFrontservicePrincipal"
  actions = ["s3:GetObject"]
  resources = [ "${aws_s3_bucket.static.arn}/*" ]

principals {
  type = "Service"
  identifiers = ["cloudfront.amazonaws.com"]
}
    condition {
      test     = "StringEquals"
      variable = "AWS:SourceArn"
      values   = [aws_cloudfront_distribution.static_website.arn]
    }
}
}
resource "aws_s3_bucket_public_access_block" "static_access" {
  bucket = aws_s3_bucket.static.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
resource "aws_s3_bucket_acl" "static_acl" {
  depends_on = [
    aws_s3_bucket_ownership_controls.static_ownership,
    aws_s3_bucket_public_access_block.static_access,
  ]

  bucket = aws_s3_bucket.static.id
  acl    = "public-read"
}

