import pandas
import logging
from flask import abort






def voir_csv(csv):


    """This function return the CSV file in Pandas data format
        Rename and delete unusual columns. """

        
    logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv, sep=';',
                                header=1,
                                usecols=[3, 4, 5, 7],
                                names=['station', 'ligne',
                                'direction', 'heure_depart'])                                                
    return db_tam

db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')

# print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'))


def city_station():


    """ This function displays all the stations. """

    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    station_list = list(set(db_tam['station'].tolist()))
    return station_list


print(city_station())


def prochain_transport(station):


    """ This function order the csv file to make some request, and answer
        about the next transports. """


    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    db_tam = db_tam.loc[db_tam['station'].isin([station])]
    result = []
    for i in range(len(db_tam)):
        resultat = {}
        resultat["heure_depart"] = str(db_tam.iloc[i][3])
        resultat["station"] = str(db_tam.iloc[i][0])
        resultat["ligne"] = str(db_tam.iloc[i][1])
        result.append(resultat)
    return result


# print(prochain_transport('GARE ST-ROCH T1'))


def depart_arrivee(station):


    """This function order the csv file to make some request, and answer
        about the next transports for a direction given. """


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


# print(depart_arrivee('GARE ST-ROCH T1'))


def station_inall(station, db_tam):

    """ This function checks if the stop name is in the database.
    Parameters : a stop name (station), a database (db_tam) 
    Returns : True or False 
    Exemple : 'COMEDIE' returns True, 'COM' returns False """


    logging.info(f"Vérifier si la station existe")
    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv') 
    # station = station.lower()
    stations = list(set(db_tam['station'].to_list()))
    if station in stations:
        return True
    else:
        return False

# print(station_inall('BOUTONNET', db_tam))

def ligne_inall(ligne, db_tam):

    """ This function checks if the route short name is in the csv """


    logging.info(f"Vérifier si la ligne existe")
    lignes=list(set(db_tam['ligne'].to_list()))
    if int(ligne) in lignes:
        return True
    else :
        return False

# print(ligne_inall('1', db_tam))


def station_tojson(station, db_tam):
    station = db_tam[(db_tam["station"] == station)].head(1)
    result = {}
    result['station'] = str(station.iloc[i][0])
    return station

