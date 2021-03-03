import pandas
from flask import abort
import logging

def voir_csv(csv):
    
    """This function return the CSV file in Pandas data format """

    # logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv,sep =';', header=2, names=['course', 'stop_code', 'stop_id',
                                                   'station', 'ligne',
                                                   'destination', 'direction_id',
                                                   'is_theorical','heure_depart',
                                                    'delay_sec','dest_arr_code'])
    return db_tam

# print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')) 

def city_station():

    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    station_list = set(db_tam['station'].tolist())
    return station_list

print(city_station())


# def prochain_transport():
#     """This function order the csv file to make some request, and answer
#     """
#     db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
#     db_tam = db_tam.loc[db_tam['station'].isin([station])].sort_values(['heure_depart'], ascending=False)
#     resultat = {}
#     resultat["heure_depart"] = str(db_tam.iloc[0][8])
#     resultat["station"] = str(db_tam.iloc[0][3])
#     resultat["ligne"] = str(db_tam.iloc[0][4])
#     resultat["destination"] = str(db_tam.iloc[0][5])
#     return resultat

# print(prochain_transport())



# def depart_arrivee():