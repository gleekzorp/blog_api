from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
# hash passwords
bcrypt = Bcrypt()

from .BlogpostModel import BlogpostModel, BlogpostSchema
from .UserModel import UserModel, UserSchema