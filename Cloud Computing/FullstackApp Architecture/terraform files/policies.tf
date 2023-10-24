resource "aws_iam_policy" "s3_access_policy" {
  name        = "EC2RDSandS3AccessPolicy"
  path        = "/"
  description = "Policy for EC2 to access RDS and S3"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
           "rds:DescribeDBInstances",
          "rds:CreateDBSnapshot",
          "rds:RestoreDBInstanceToPointInTime",
          "s3:GetObject",
          "s3:ListBucket",
        ]
        Effect   = "Allow"
        Resource = "*" # arn:aws:s3:::learningbucketforuni/
      },
    ]
  })
}
resource "aws_iam_policy_attachment" "ec2_rds_s3_policy_attachment" {
  name       = "EC2RDSandS3Attachment"
  roles      = [aws_iam_role.ec2s3accessrole.name]
  policy_arn = aws_iam_policy.s3_access_policy.arn
}