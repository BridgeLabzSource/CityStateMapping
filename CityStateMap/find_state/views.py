from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from geopy.geocoders import Nominatim
import googlemaps
from find_state.spelling_checker import check_spelling
from fastapi import APIRouter
from find_state.models import City
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/states/")
def get_state(city: City):
    try:
        if len(city.city_name) > 0 and city.city_name.isalpha():
            correct_city_name = check_spelling(city.city_name)
            print(correct_city_name)
            geo_locator = Nominatim(user_agent="geoapiExercises")
            location = geo_locator.geocode(correct_city_name, addressdetails=True)
            # print(location.raw)
            return JSONResponse(status_code=status.HTTP_200_OK,content=f"State:- {location.raw['address']['state']}")
        else:
            raise KeyError
    except KeyError as exception:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content="give a proper city name")
    except Exception as exception:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                            content=f"error occurred due to {exception.__str__()}")


class FindStateView(APIView):
    """
    View handles the request to know the state of the given city name
    """

    def get(self, request):
        """
        Google maps library is used to send the request to geocoding api to get the name of the
        state to which the given city (name) belongs
        :param request:- city name whose state name is to be found
        :return:- state name else appropriate exception will be thrown in the response
        """
        gmaps = googlemaps.Client(key="api_key_goes_here")
        location = gmaps.geocode(request.data['city'])
        print(location)
        return Response(location.raw['address']['state'])

    def post(self, request):
        """
        Geopy library is used to send the request to Nominatim to get the state name of the given city name and
        then output is converted to raw text to get the state name only
        :param request:- city name whose state is to be found
        :return:- state name else appropriate exception will be thrown in the response
        """
        try:
            correct_city_name = check_spelling(request.data['city'])
            geo_locator = Nominatim(user_agent="geoapiExercises")
            location = geo_locator.geocode(correct_city_name, addressdetails=True)
            print(location.raw)
            return Response(location.raw['address']['state'])
        except Exception as exception:
            return JsonResponse({"message": f"error occurred due to {exception.__str__()}"},
                                status=status.HTTP_400_BAD_REQUEST)
