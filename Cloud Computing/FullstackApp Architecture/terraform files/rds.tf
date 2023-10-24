data "aws_availability_zones" "available_zones" {}

resource "aws_default_subnet" "subnet_1" {
  availability_zone = data.aws_availability_zones.available_zones.names[0]
}

resource "aws_default_subnet" "subnet_2" {
  availability_zone = data.aws_availability_zones.available_zones.names[1] 
}
# security group for the database
resource "aws_security_group" "database_security_group" {
  name        = "database security group"
  description = "enable mysql/aurora access on port 3306"
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    description      = "mysql access"
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
# the subnet group for the rds instance
resource "aws_db_subnet_group" "database_subnet_group" {
  name         = "dbsubnets"
  subnet_ids   = [aws_default_subnet.subnet_1.id, aws_default_subnet.subnet_2.id]
  description  = "subnets for db"

  tags   = {
    Name = "dbsubnets"
  }
}
# create the rds instance
resource "aws_db_instance" "default" {
  allocated_storage    = 100
  db_name              = "mydb"
  engine               = "mysql"
  engine_version       = "8.0.33"
  instance_class       = "db.t2.micro"
  username             = "dbuser"
  password             = "dbpassword"
  db_subnet_group_name = aws_db_subnet_group.database_subnet_group.name
  vpc_security_group_ids = [aws_security_group.database_security_group.id]
  availability_zone = data.aws_availability_zones.available_zones.names[0]
  identifier = "maindb"
  skip_final_snapshot = false 
  allow_major_version_upgrade = true
}