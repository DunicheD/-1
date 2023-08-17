from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"base.html")

def about(request):
    return HttpResponse("<h2>О нас<h2>")


def user(request, user):
    return HttpResponse(f"<h2>Имя {user}<h2>")


def user(request, user="Undefind", age="4"):
    return HttpResponse(f"<h2>Имя {user}, Возраст {age}<h2>")
