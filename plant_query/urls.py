from django.urls import path

from .views import get_plant_data, get_location_data, get_comment_analysis, random_comment

urlpatterns = [
    path("plants/", get_plant_data),
    path("location/", get_location_data),
    path('comments/', get_comment_analysis),
    path('randomComments/', random_comment)
]
