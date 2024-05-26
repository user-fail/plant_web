from django.urls import path, include

from plant_query import urls
from .view import index

urlpatterns = [
    path("api/", include(urls)),
    path('', index)
]
