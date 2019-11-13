from django.contrib import admin
from django.urls import path , include
from graphene_django.views import GraphQLView
from .views import snippets

urlpatterns = [
    path('' ,snippets),
]