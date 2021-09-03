from django.urls import path

from find_state import views

urlpatterns = [
    path(r'state/', views.FindStateView.as_view(), name="city_map"),
]
