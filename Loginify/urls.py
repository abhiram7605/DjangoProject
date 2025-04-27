from django.urls import path
from . import views

urlpatterns = [
    path("initial/", views.hello),
    path("signup/", views.signup),
    path("signin/", views.signin, name = "signin")
]