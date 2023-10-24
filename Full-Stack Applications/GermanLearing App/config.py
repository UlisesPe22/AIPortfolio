from flask_sqlalchemy import SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
db = SQLAlchemy()