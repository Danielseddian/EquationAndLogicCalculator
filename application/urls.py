from django.urls import path, include

from . import views

app_name = "application"

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/signup/", views.SignUp.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]