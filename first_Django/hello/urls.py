from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shu", views.shu, name="shu"),
    path("<str:name>", views.greet, name="greet"),
]
