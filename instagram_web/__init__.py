from app import app
from flask import render_template
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

from instagram_web.blueprints.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix="/users")

from instagram_web.blueprints.station.views import station_blueprint
app.register_blueprint(station_blueprint, url_prefix="/station")

from instagram_web.blueprints.booking.views import booking_blueprint
app.register_blueprint(booking_blueprint, url_prefix="/booking")

from instagram_web.blueprints.pumps.views import pumps_blueprint
app.register_blueprint(pumps_blueprint, url_prefix="/pumps")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')
