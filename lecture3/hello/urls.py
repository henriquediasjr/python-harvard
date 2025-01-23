from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),


    path("henrique", views.henrique, name="henrique"),
    path("niara", views.niara, name="niara"),

]