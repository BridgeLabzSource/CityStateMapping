from nltk.metrics.distance import edit_distance
from find_indian_state.indian_cities import get_cities_name


def check_spelling(city_name):
    """
    Function is used to correct the city name using nltk. Distance is calculated between the city name provided by the
    user and the correctly spelled cities name and then the minimum distance word is chosen as the correctly spelled
    city name
    """
    correct_spellings = get_cities_name()
    distance = ((edit_distance(city_name, word), word) for word in correct_spellings)
    city_name = min(distance)
    return city_name
