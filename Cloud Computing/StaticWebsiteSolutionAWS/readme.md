# Static Website Architecture with AWS CloudFront and Terraform

This Terraform script deploys an architecture for hosting a static website using Amazon Web Services (AWS) CloudFront for content delivery and Amazon S3 for storage. This architecture provides fast and reliable website hosting with content caching. In this repository you can find the terraform files and a pdf explaining the architecture. 

## Prerequisites

Before you get started, ensure you have the following prerequisites:

1. **AWS Account**: You must have an AWS account. 

2. **Terraform Installed**: Install Terraform on your local machine. 

3. Get your AWS keys properly setup 

## Getting Started

Follow these steps to replicate and launch the architecture:

1. **Download the files**

2. Open Visual Studio or any coding enviorment and in the terminal write the following commands:
      * terraform init
      * terraform plan (optional)
      * terraform apply
3. Paste the policy on the S3 bucket:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mystaticbucketforuni/*"
        }
    ]
}






