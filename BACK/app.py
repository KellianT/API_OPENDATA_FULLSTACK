from flask import Flask, jsonify
from flask import render_template
import logging
from flask import Flask, abort, jsonify
from fonctions import prochain_transport
from fonctions import depart_arrivee
app = Flask(__name__)


# @app.route('/')
# def entry_point():
#     return render_template('./app.html')

@app.route('/')
def hello_world():
   return jsonify('Hello, World!')

# #il manque la premiere route
# @app.route('/city/<stations>')
# def station():
#     return jsonify(city_station())


@app.route('/city/station/<stations>')
def station(stations):
    return jsonify(prochain_transport(stations))

@app.route('/city/next/<station>')
def next_station(station):
    return jsonify(depart_arrivee(station))



if __name__ == '__main__':
    app.run(debug=True)
