from mongoengine import *

class User(Document):
    user_name = StringField(max_length=200, required=True)
    user_id = StringField(max_length=200, required=True)
    user_password = StringField(max_length=200, required=True)
