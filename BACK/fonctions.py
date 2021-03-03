import pandas
from flask import abort
import logging

def voir_csv(csv):
    
    """This function return the CSV file in Pandas data format """

    logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv,sep =';')
    return db_tam

print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')) 


def city_stations():
    liste_stations = db_tam["stop_name"] == 
