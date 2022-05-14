from django.shortcuts import render


def list(request):
    return render(request, 'frontend/list.html')


def user_login(request):
    return render(request, 'frontend/login.html')


def user_register(request):
    return render(request, 'frontend/signup.html')