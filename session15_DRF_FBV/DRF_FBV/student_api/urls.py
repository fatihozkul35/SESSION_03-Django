from django.urls import path
from .views import home, student_api, student_api_get_update_delete, path_api, student_create_api, student_delete_api, student_list_api, student_partial_udate, student_update_api

urlpatterns = [
    path('', home),
    path('student/', student_api),
    path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
    path('path/', path_api),
    path('student_list', student_list_api),
    path('student_create', student_create_api),
    path('student_update/<int:pk>', student_update_api),
    path('student_delete/<int:pk>', student_delete_api),
    path('student_patch/<int:pk>', student_partial_udate),    
]
