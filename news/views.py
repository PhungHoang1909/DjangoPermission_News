from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CompanyLoginForm
import requests


# Create your views here.
class CustomLoginView(LoginView):
    form_class = CompanyLoginForm
    template_name = "news/login.html"


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def news_home(request):
    api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=eb39576156744e22addb8a389e485666"
    response = requests.get(api_url)
    news_data = response.json()
    articles = news_data.get("articles", [])
    return render(request, "news/home.html", {"articles": articles})
