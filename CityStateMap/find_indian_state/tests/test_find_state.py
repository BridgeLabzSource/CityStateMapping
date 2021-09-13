import unittest

from find_indian_state.views import FindState


class TestFindState(unittest.TestCase):
    def test_get_state_with_city_name(self):
        city_name = "Ajmer"
        response = FindState.get_state_by_city(city_name)
        self.assertEqual("Rajasthan",response)

    def test_get_state_with_incorrectly_spelled_city_name(self):
        city_name = "Bombai"
        response = FindState.get_state_by_city(city_name)
        self.assertEqual("Maharashtra", response)

    def test_get_state_with_empty_string_as_city_name(self):
        city_name = ""
        response = FindState.get_state_by_city(city_name)
        self.assertEqual("Please enter some city name", response)

    def test_get_state_with_numeric_string_as_city_name(self):
        city_name = "122435"
        response = FindState.get_state_by_city(city_name)
        self.assertEqual("Please enter some city name", response)

    def test_get_state_with_given_coordinates(self):
        latitude="12.9716° N"
        longitude="77.5946° E"
        response = FindState.get_state_by_coordinates(latitude,longitude)
        self.assertEqual("Karnataka", response)

    def test_get_state_with_invalid_coordinates(self):
        latitude="12.aa54° N"
        longitude="77.235js° E"
        response = FindState.get_state_by_coordinates(latitude,longitude)
        self.assertEqual("error occurred due to Must be a coordinate pair or Point", response)

    def test_get_state_with_empty_string_as_coordinates(self):
        latitude=""
        longitude=""
        response = FindState.get_state_by_coordinates(latitude,longitude)
        self.assertEqual("Please enter valid coordinates", response)
