import pandas
from flask import abort
import logging

def voir_csv(csv):
    
    """This function return the CSV file in Pandas data format """

    logging.info("création de la base de données")
    db_tam = pandas.read_csv(csv,sep =';', header=2, names=['course', 'stop_code', 'stop_id',
                                                   'station', 'ligne',
                                                   'destination', 'direction_id',
                                                   'is_theorical','heure départ',
                                                    'delay_sec','dest_arr_code'])
    return db_tam

print(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')) 


# def station():
#     """This function permit to convert the csv file to list
#     """
#     df = voir_csv()
#     choix_station = set(df['stop_name'].tolist())
#     return choix_station
# print(choix_station)

# def city_stations():
# df = voir_csv()
#     df = df.loc[df["station"].isin(
#         [pays])].sort_values(["year"], ascending=False)
#     resultat = {}
#     resultat["country"] = str(df.iloc[0][1])
#     resultat["year"] = int(df.iloc[0][2])
#     resultat["value"] = float(df.iloc[0][4])
#     return resultat
