from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("coffee/<slug:slug>/", views.coffee_detail, name="coffee_detail"),
]
