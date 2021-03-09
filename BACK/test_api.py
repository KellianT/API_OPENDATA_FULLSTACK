import unittest
from app import app


class TestApiFlask(unittest.TestCase):

    def setUp(self):
        """ def setup run app
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """ def status_code test if path is ok "/"
         """
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        # ".status_code = renvoie, si marche = 200 (ok)


    def test_home_type(self):
        """ test_home_type test if te app is j.son content
         """
        result = self.app.get('/city/next/')
        self.assertEqual(result.content_type, 'application/json')


# /city/next/:
    def test_home_city_next(self):
        """by_station if station display
        """
        result = self.app.get('/city/next/')
        # print(result.data)
        self.assertTrue(b'direction' in result.data)
        self.assertTrue(b'station' in result.data)
        self.assertTrue(b'heure_depart' in result.data)



if __name__ == '__main__':
    unittest.main()