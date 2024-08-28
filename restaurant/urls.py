from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu-items/", views.MenuView.as_view()),
    path("menu-items/<int:pk>", views.MenuSingleView.as_view()),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
