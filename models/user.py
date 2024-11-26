from db import db
from sqlalchemy import text
from marshmallow import Schema, fields

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(250), nullable = False, unique = True)
    age = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'), onupdate = db.func.current_timestamp())

class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str()
    email = fields.Email()
