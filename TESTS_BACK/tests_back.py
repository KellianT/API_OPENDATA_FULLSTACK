import unittest
import sys
sys.path.append('C:/Users/utilisateur/Desktop/Python/Projets/API_OPENDATA_FULLSTACK/BACK')
from fonctions import voir_csv
from fonctions import city_station
from fonctions import prochain_transport
import pandas

df = voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv')

class TestMethods(unittest.TestCase):

    def test_voir_csv(self):
        """ Test if the CSV file is in pandas format
            and if the column 'station' is in the CSV """

        self.assertIsInstance(voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'), pandas.core.frame.DataFrame)
        self.assertTrue("station" in voir_csv('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'))   


    # def test_city_station(self):
    #     """This function display all stations"""

    #     # self.assertIsInstance(city_station())
    #     # self.assertIsNot
    #     self.assertEqual(city_station(), {"ligne" : "1",
    #                                     "direction" : "HAUTS DE MASSANE"})


    # def test_prochain_transport(self):
    #     """This function order the csv file to make some request, and answer
    #     about the next transports.
    #     """
    #     self.assertFalse(prochain_transport()
        #self.assertFalse(prochain_transport("CORUM T")
        #self.assertTrue(prochain_transport)



if __name__ == '__main__':
    unittest.main()
