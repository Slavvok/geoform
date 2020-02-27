from django.contrib import admin
from django.urls import path
from .views import GeoFormView, GetGeoCodeView

urlpatterns = [
    path('main/', GeoFormView.as_view()),
    path('get_geocode/', GetGeoCodeView.as_view())
]
