from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout


def login_form(request, error=None):
    return render(request, "login.html")


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        next_page = request.POST.get('next', '/')
        return redirect(next_page)
    else:
        return login_form(request, error="Invalid user name or password")


def index(request):
    if request.method == 'POST':
        return authenticate_user(request)
    else:
        logout(request)
        return login_form(request)
