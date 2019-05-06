from flask import Blueprint, render_template, jsonify, url_for
from models.pumps import Pumps
from models.station import Station

pumps_blueprint = Blueprint('pumps',
                            __name__,
                            template_folder='templates')


@pumps_blueprint.route('/new', methods=['GET'])
def new():
    pass

@pumps_blueprint.route('/<pumpname>/<stationid>', methods=['POST'])
def create(pumpname, stationid):
    pump = Pumps()
    pump.name = pumpname
    pump.station_id = stationid
    pump.save()
    return jsonify({
            "message": "Successfully make a new item."
        }), 200


@pumps_blueprint.route('/show', methods=["GET"])
def show():
    pump_object = []
    pump = Pumps.select()
    for i in pump:
        pump_object.append(
            {
                'id': i.id,
                'pump_name': i.name,
                'station_id': i.station_id,
                "station_name": i.station.name
            }
        )
    return jsonify({
            "message": "Successfully update a new item.",
            "pump_object": pump_object
        }), 200


@pumps_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@pumps_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@pumps_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass