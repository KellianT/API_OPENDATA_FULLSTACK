import pandas
from flask import abort
import logging

def voir_csv(csv):
    
    """This function return the CSV file in Pandas data format """

    logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv, header=0, names=['course';'stop_code'; 'stop_id';
                                                   'stop_name'; 'route_short_name';
                                                   'trip_headsign'; 'direction_id';
                                                   'is_theorical';'departure_time';
                                                    'delay_sec';'dest_arr_code'])
    return db_tam

print(voir_csv("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv"))
# df = pandas.read_csv("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv")
# print(df.head()
