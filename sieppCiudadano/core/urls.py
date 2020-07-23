from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', notasView.as_view(), name="inicio"),
    path('eje/<str:idEje>', EjeView.as_view(), name="Eje"),
]
