from django.urls import path
from .views import CustomLoginView, logout_view, news_home

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("", news_home, name="home"),
]
