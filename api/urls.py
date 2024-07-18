from django.urls import path
from rest_framework import routers
from api import viewsModelSerializer as views


urlpatterns =[
    path('saveword',views.TranslateWordView.as_view()),
]