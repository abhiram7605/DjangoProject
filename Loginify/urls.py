from django.urls import path
from . import views

urlpatterns = [
    path("initial/", views.hello),
    path("signup/", views.signup),
    path("signin/", views.signin, name = "signin"),
    path("all_data/", views.all_data),
    path("singleuser/<str:pk>/", views.single_user)
]