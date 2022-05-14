from django.urls import path
from . import views

urlpatterns = [
    path('overview/',views.apiOverview, name='api-overview'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout),
    path('signup/', views.signup, name='signup'),
]