from django.urls import path
from Games_List import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Games_List/<name>", views.test_code, name="hello_there"),
]
