terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {
  region = "eu-central-1"
}

resource "aws_default_vpc" "default_vpc" {

  tags = {
    Name = "default vpc"
  }
}
resource "aws_security_group" "security_group" {
  name        = "security group"
  description = "enable http access on port 80"
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    description      = "http access"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = -1
      cidr_blocks      = ["0.0.0.0/0"]
  }

  tags   = {
    Name = "security_group"
  }
}