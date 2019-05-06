from models.base_model import BaseModel
import peewee as pw


class Station(BaseModel):
    name = pw.CharField(null=True)
    location = pw.CharField(unique=True)
    contact = pw.CharField(null=True)
