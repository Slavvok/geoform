from django.contrib import admin
from django.urls import path
from .views import MainView, GetGeoCodeView

urlpatterns = [
    path('main/', MainView.as_view()),
    path('get_geocode/', GetGeoCodeView.as_view())
]
