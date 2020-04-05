import unittest

from city_functions import city_country


class LocationTestCase(unittest.TestCase):

    def test_city_country(self):
        """Is a combination like 'berlin' and 'germany' properly formatted?"""
        formatted_location = city_country('berlin', 'germany')
        self.assertEqual(formatted_location, 'Berlin, Germany')

    def test_city_country_population(self):
        """
        Is a combination like 'berlin', 'germany' and 5000000 properly
        formatted?
        """
        formatted_location = city_country('berlin', 'germany', 5000000)
        self.assertEqual(formatted_location,
                         'Berlin, Germany ‒ population 5000000')


if __name__ == '__main__':
    unittest.main()
