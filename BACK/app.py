import logging
import pandas
from flask_cors import CORS, cross_origin
from flask import render_template
from flask import Flask, abort, jsonify
from fonctions import prochain_transport
from fonctions import depart_arrivee
from fonctions import city_station




app = Flask(__name__,)
CORS(app)


logging.basicConfig(
    filename='app_opendata.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)



@app.route('/')
@cross_origin()
def entry_point():


    """ link html and route 3. """

    return render_template('./route3.html')



@app.route('/')
@cross_origin()
def entry_point_deux():


    """ link html and route 2. """

    return render_template('./route2.html')



@app.route('/')
@cross_origin()
def entry_point_une():


    """ link html and route 1. """

    return render_template('./route1.html')



@app.route('/city/stations')
@cross_origin()
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
@cross_origin()
def next_transport_station(station):

    
    """ Liste les prochains transports à cette station """


    return jsonify(prochain_transport(station))


@app.route('/city/next/')
@cross_origin()
def next_station_data():


    """ Prochain transport vers une direction (station, ligne, temps, destination) """

    return jsonify(depart_arrivee())



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
