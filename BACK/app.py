import logging
import pandas
from flask import Flask, jsonify
from flask import render_template
from flask import Flask, abort, jsonify
from fonctions import prochain_transport
from fonctions import depart_arrivee
from fonctions import city_station

# from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# CORS(app)


logging.basicConfig(
    filename='app_opendata.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)

@app.route('/')
def entry_point():
    return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
   return jsonify('Hello, World!')

#il manque la premiere route
@app.route('/city/stations')
def all_stations():


    """ Liste tous les arrêts """

    # db_tam = fonctions.voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    # station = station.title()
    # if fonction.station_inall(station, db_tam):
    #     station = fonction.station_tojson(station, db_tam)
    #     return jsonify(station)
    # else:
    #     logging.warning("Erreur 404: fonction station pas ok")
    #     abort(404)
    return jsonify(city_station())


@app.route('/city/station/<station>')
def next_transport_station(station):

    
    """ Liste les prochains transports à cette station """


    return jsonify(prochain_transport(station))


@app.route('/city/next/<station>')
def next_station_data(station):


    """ Prochain transport vers une direction (station, ligne, temps, destination) """

    return jsonify(depart_arrivee(station))



if __name__ == '__main__':
    app.run(debug=True)
