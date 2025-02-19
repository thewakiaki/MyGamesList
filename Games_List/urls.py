from django.urls import path
from Games_List import views

urlpatterns = [
    path("", views.home, name="home"),
]
