from nltk.metrics.distance import edit_distance
from find_state.indian_cities import get_cities_name


def check_spelling(city_name):
    correct_spellings = get_cities_name()
    distance = ((edit_distance(city_name, word), word) for word in correct_spellings)
    # city_names=[city[1] for city in distance if city[0]<3]
    city_name = min(distance)
    return city_name
