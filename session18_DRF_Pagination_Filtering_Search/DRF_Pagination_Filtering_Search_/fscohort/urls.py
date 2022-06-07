from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView, CourseListCreateAPIView

urlpatterns = [
    
    path("", StudentListCreateAPIView.as_view(), name="list"),
    path("list_api/<int:id>", StudentDetailAPIView.as_view(), name="detail"),
    path("courses/", CourseListCreateAPIView.as_view(), name="courses"),
    
]

