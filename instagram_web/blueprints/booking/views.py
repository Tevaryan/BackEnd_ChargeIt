from flask import Blueprint, render_template, jsonify, url_for
from models.booking import Bookings


booking_blueprint = Blueprint('booking',
                            __name__,
                            template_folder='templates')


@booking_blueprint.route('/new', methods=['GET'])
def new():
    pass

@booking_blueprint.route('/<stationid>/<pumpid>/<timings>', methods=['POST'])
def create(stationid,pumpid,timings):
    # booking = Bookings()
    # booking.station_id = stationid
    # booking.pump_id = pumpid
    # booking.timing = timings 
    # booking.save()
    Bookings.create(station_id = stationid, pump_id = pumpid, timing = timings)
    return jsonify({
        "message": "Successfully make a new item."
        }), 200


@booking_blueprint.route('/show', methods=["GET"])
def show():
    booking_object = []
    booking = Bookings.select()
    for i in booking:
        booking_object.append(
            {
                'id': i.id,
                'timing': i.timing,
                'pump_id': i.pump_id,
                'pump_name': i.pump.name,
                'station_id': i.station_id,
                "station_name": i.station.name,
                "user_id": i.user_id
            }
        )
    return jsonify({
            "message": "Successfully update a new item.",
            "booking_object": booking_object
        }), 200


@booking_blueprint.route('/', methods=["GET"])
def index():
    pass


@booking_blueprint.route('/edit/<id>/<timings>', methods=['POST'])
def edit(id, timings):
    booking = Bookings.get(Bookings.id == id)
    booking.timing = timings
    booking.save()
    return jsonify({
        "message": "Successfully changed."
        }), 200


@booking_blueprint.route('/<id>', methods=['POST'])
def update(id):
    booking = Bookings.get(Bookings.id == id)
    booking.delete_instance()
    booking.save()
    return jsonify({
        "message": "Successfully deleted."
        }), 200

@booking_blueprint.route('bookTiming/<userid>/<timings>/<pumpid>/<stationid>', methods=['POST'])
def booktiming(userid, timings, pumpid, stationid):
    booking = Bookings.get(Bookings.timing == timings, Bookings.pump_id == pumpid, Bookings.station_id == stationid)
    booking.user_id = userid
    booking.save()
    return jsonify({
        "message": "Successfully booked"
        }), 200

@booking_blueprint.route('showbookedtiming/<id>', methods=['get'])
def showbookedtiming(id):
    booking_object = []
    booking = Bookings.select().where(Bookings.user_id == id)
    for i in booking:
        booking_object.append(
            {
                'id': i.id,
                'timing': i.timing,
                'pump_id': i.pump_id,
                'pump_name': i.pump.name,
                'station_id': i.station_id,
                "station_name": i.station.name,
                "user_id": i.user_id
            }
        )

    return jsonify({
        "message": "Successfully sent.",
        "booking_object": booking_object
        }), 200

@booking_blueprint.route('cancelTiming/<userid>/<timings>/<pumpid>/<stationid>', methods=['POST'])
def canceltiming(userid, timings, pumpid, stationid):
    booking = Bookings.get(Bookings.timing == timings, Bookings.pump_id == pumpid, Bookings.station_id == stationid)
    booking.user_id = null
    booking.save()
    return jsonify({
        "message": "Successfully cancelled"
        }), 200