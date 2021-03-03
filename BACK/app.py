from flask import Flask, render_template
from fonctions import ouvrir_csv
from Flask import jsonify
import pandas
import fonctions as fct
app = Flask(__name__)

logging.basicConfig(
    filename='API_OpenData.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)

logging.info("Démarrage de l'API")

db_tam = fct.voir_csv("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv")




@app.route('/')
def entry_point():
    return render_template('./app.html')



    

@app.route('/hello_world')
def hello_world():
    return 'Hello World'





@app.route('/city/stations/')





@app.route('/city/stations/<station>')

    """ liste les prochains transports à cette station
        sans destination.
    """
def next():
    return jsonify(dico(country))






    @app.route('/city/next?line=&station=&direction=')
    
    """ liste les prochains transports à cette station
        avec destination.
    """
def next_dest():
    return jsonify(dico(country))

if __name__ == '__main__':
    app.run(debug=True)