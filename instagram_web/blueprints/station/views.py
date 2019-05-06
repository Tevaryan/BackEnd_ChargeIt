from flask import Blueprint, render_template, jsonify, url_for
from models.station import Station


station_blueprint = Blueprint('station',
                            __name__,
                            template_folder='templates')


@station_blueprint.route('/new', methods=['GET'])
def new():
    pass

@station_blueprint.route('create/<contacted>/<stationname>/<located>', methods=['POST'])
def create_new_station(contacted, stationname, located):

    station = Station()
    station.contact = contacted
    station.name = stationname
    station.location = located
    station.save()
    return jsonify({
        "message": "Successfully make a new item."
        }), 200


@station_blueprint.route('/show', methods=["GET"])
def show():
    station_object = []
    station = Station.select()
    for i in station:
        station_object.append(
            {
                'id': i.id,
                'name': i.name
            }
        )
    return jsonify({
            "message": "Successfully update a new item.",
            "station_object": station_object
        }), 200


@station_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@station_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@station_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
