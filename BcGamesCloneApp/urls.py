from django.urls import path
from BcGamesCloneApp import views

urlpatterns = [
    path(route='', view=views.index, name="index"),
]
