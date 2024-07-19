from django.urls import path
from rest_framework import routers
from api import viewsModelSerializer as views


urlpatterns =[
    path('saveword',views.TranslateWordViewCR.as_view()),
    path('saveword_elements/<int:id>',views.TranslateWordViewUD.as_view())
]