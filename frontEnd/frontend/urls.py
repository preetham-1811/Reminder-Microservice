from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
	path('login/', views.user_login, name="login"),
	path('signup/', views.user_register, name="register"),
]
