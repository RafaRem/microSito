from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', notasView.as_view(), name="inicio"),
    path('inform/<str:inf>', notasView.as_view(), name="informe"),
    path('eje/<str:idEje>', EjeView.as_view(), name="Eje"),
    path('covid', CovidView.as_view(), name="covid"),
    url(r'^.*/$', notasView.as_view())
    
]
