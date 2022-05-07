from django.urls import path
from .views import student_page, okul

urlpatterns = [
    path('', student_page, name='student'),
    path('okul/', okul, name='student'),
]