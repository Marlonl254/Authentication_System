from django.urls import path
from . import views
 
urlpatterns = [
    path("home/", views.HomePage, name="homepage"),
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("", views.Login, name="login")
    
]