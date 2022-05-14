from django.urls import path, include
from . import views

urlpatterns = [
	path('reminder/', views.List, name="reminder-list"),
	path('reminder/<str:pk>/', views.Detail, name="reminder-detail"),
	path('create-reminder/', views.Create, name="reminder-create"),

	path('update-reminder/<str:pk>/', views.Update, name="reminder-update"),
	path('delete-reminder/<str:pk>/', views.Delete, name="reminder-delete"),
]
