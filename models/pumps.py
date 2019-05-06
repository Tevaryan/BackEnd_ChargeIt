from models.base_model import BaseModel
import peewee as pw
from models.station import Station


class Pumps(BaseModel):
    name = pw.CharField(null=False)
    picture = pw.CharField(default='profile-placeholder.jpg')
    station = pw.ForeignKeyField(Station, backref="station")

