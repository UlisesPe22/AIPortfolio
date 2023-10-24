resource "aws_security_group" "ec2_security_group" {
  name        = "ec2 security group"
  description = "enable ec2 instance  access on port 3306"
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    description      = "ec2 access to port 3306"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    security_groups  = [aws_security_group.security_group.id]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = -1
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags   = {
    Name = "security_group_database"
  }
}

resource "aws_instance" "MyMainEC2Instance" {
  ami           = "ami-05705f8465db448b7"
  instance_type = "t2.micro"
   vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  tags = {
    "Name"= "MyMainEC2Instance"
  }
}
resource "aws_iam_role" "ec2s3accessrole" {
  name = "rolesforuniapp"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })

  tags = {
    tag-key = "s3_access_role"
  }
}
resource "aws_iam_instance_profile" "profileInstance" {
  name = "profile"
  role = aws_iam_role.ec2s3accessrole.name
}

