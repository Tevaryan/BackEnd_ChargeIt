from models.base_model import BaseModel
import peewee as pw
from models.station import Station
from models.pumps import Pumps
from models.user import User

class Bookings(BaseModel):

    timing = pw.CharField(null= True)
    station = pw.ForeignKeyField(Station, backref="station")
    pump = pw.ForeignKeyField(Pumps, backref="pumps")
    user = pw.ForeignKeyField(User, backref="user", null = True)
