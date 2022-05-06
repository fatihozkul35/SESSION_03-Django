
from .views import homeFunction
from django.urls import path

urlpatterns = [
    path("",homeFunction)
]