import pandas
from flask import abort
import logging

def voir_csv(csv):
    """This function return the CSV file in Pandas data format
        Rename and delete unusual columns.
    """

    # logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv, sep =';',
                                header=1,
                                usecols=[3,4,5,7],
                                names=['station', 'ligne', 
                                'direction','heure_depart'])
                                                    
    # db_tam = db_tam.rename(columns={
    #                     "stop_name":"station",
    #                     "route_short_name":"ligne",
    #                     "trip_headsign":"destination",
    #                     "departure_time":"heure_depart"},inplace=True)
    return db_tam

# print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')) 

def city_station():
    """ This function displays all the stations.
    """

    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    station_list = set(db_tam['station'].tolist())
    return station_list

# print(city_station())


def prochain_transport(station):
    """This function order the csv file to make some request, and answer
        about the next transports.
        Range le résultat dans un dictionnaire pour lire j.son
        iloc = faire une boucle qui ajoute mon résultat par rapport à ce
        que je veux récupérer comme valeur 
        pour qu'il les ajoute dans mon dico.
    """

    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    db_tam = db_tam.loc[db_tam['station'].isin([station])]

    result = []

    for i in range(len(db_tam)):
        resultat = {}
        resultat["heure_depart"] = str(db_tam.iloc[i][3])
        resultat["station"] = str(db_tam.iloc[i][0])
        resultat["ligne"] = str(db_tam.iloc[i][1])
        resultat["direction"] = str(db_tam.iloc[i][2])
        result.append(resultat)
    
    return result

# print(prochain_transport('GARE ST-ROCH T1'))


# # def depart_arrivee():
#     """This function order the csv file to make some request, and answer
#         about the next transports for a destination given.
    # """