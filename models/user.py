from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=False)
    password = pw.CharField(null=True)
    picture = pw.CharField(default='profile-placeholder.jpg')

    firstname = pw.CharField(null=True)
    lastname = pw.CharField(null=True)
    location = pw.CharField(null=True)
    contact = pw.IntegerField(null=True)
