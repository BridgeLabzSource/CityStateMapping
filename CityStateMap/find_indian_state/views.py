from geopy.geocoders import Nominatim
from find_indian_state.spelling_checker import check_spelling
import logging

logger = logging.getLogger('user_exceptions')
logger.setLevel(logging.DEBUG)
log_handlers = {
    "file_debug": logging.FileHandler("exceptions.log".format(name=__name__, level="DEBUG"), mode="w"),
}
logger.addHandler(log_handlers['file_debug'])


class FindState:
    """
    class handles the request to know the state by either using the city name or by using coordinates whichever provided
    by the user
    """

    def __init__(self):
        pass

    @staticmethod
    def get_state_by_city(city_name):
        """
        To retrieve the state name of the given city name provided by the user, request is made to the Nominatim library
        using geopy with the correctly spelled city name, on success response with state name is returned else
        appropriate exception will be returned. City name given by user is checked for any spelling mistake using nltk
        and if there is any then best possible correctly spelled city name is used to retrieve the state
        :param city_name:- city name whose state is to be found
        :return:- state name else appropriate exception will be thrown in the response
        """
        try:
            if len(city_name) == 0 or not city_name.isalpha():
                raise KeyError
            else:
                correct_city_name = check_spelling(city_name)
                geo_locator = Nominatim(user_agent="geopy_exercise")
                location = geo_locator.geocode(correct_city_name, addressdetails=True, exactly_one=True)
                return location.raw['address']['state']
        except KeyError as exception:
            logger.exception(exception.__traceback__)
            return "Please enter some city name"
        except Exception as exception:
            logger.exception(exception.__traceback__)
            return f"error occurred due to {exception.__str__()}"

    @staticmethod
    def get_state_by_coordinates(latitude, longitude):
        """
        To get the state name from the latitude and longitude provided by the user, request is made to the Nominatim
        library using geopy, on success response with state name is returned else appropriate exception will be returned
        :param latitude:- latitude of location whose state is to be found
        :param longitude:- longitude of location whose state is to be found
        :return:- state name else appropriate exception will be thrown in the response
        """
        try:
            if len(latitude) == 0 or len(longitude) == 0:
                raise KeyError
            else:
                coordinates = latitude + "," + longitude
                geo_locator = Nominatim(user_agent="geoapi_exercises")
                location = geo_locator.reverse(coordinates, exactly_one=True)
                return location.raw['address']['state']
        except KeyError as exception:
            logger.exception(exception.__traceback__)
            return "Please enter valid coordinates"
        except Exception as exception:
            logger.exception(exception.__traceback__)
            return f"error occurred due to {exception.__str__()}"
