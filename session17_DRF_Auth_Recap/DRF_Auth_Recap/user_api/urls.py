from django.urls import path
from .views import RegisterView, logout_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',obtain_auth_token, name='login'),
    path('logout/',logout_view, name='logout'),
]