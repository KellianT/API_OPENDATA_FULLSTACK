import pandas
from flask import abort
import logging

def voir_csv(csv):
    
    """This function return the CSV file in Pandas data format """

    # logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv,sep =';', header=2, names=['course', 'stop_code', 'stop_id',
                                                   'station', 'ligne',
                                                   'destination', 'direction_id',
                                                   'is_theorical','heure départ',
                                                    'delay_sec','dest_arr_code'])
    return db_tam

# print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')) 

def city_station():
    db_tam = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')
    station_list = set(db_tam['station'].tolist())
    return station_list

print(city_station())


# def dico(station):
#     """This function order the csv file to make some request, and answer
#     """
#     df = voir_csv()
#     df = df.loc[df["station"].isin(
#         [transport])].sort_values(["heure départ"], ascending=False)
#     resultat = {}
#     resultat["country"] = str(df.iloc[0][1])
#     resultat["year"] = int(df.iloc[0][2])
#     resultat["value"] = float(df.iloc[0][4])
#     return resultat
