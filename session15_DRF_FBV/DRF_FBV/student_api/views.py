from functools import partial
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import serializers

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse('<h1>API Page</h1>')


@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
   
    
@api_view(['GET'])
def student_list_api(request):
    students = Student.objects.filter(path=1)
    serializer = StudentSerializer(students, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def student_create_api(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'message':f"{serializer.validated_data.get('number')} Created!!!!!!!"
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
    

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # student = Student.objects.filter(pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(
            student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)


@api_view(['GET', 'POST'])
def path_api(request):
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status

    if request.method == 'GET':
        paths = Path.objects.all()
        serializer = PathSerializer(
            paths, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # from pprint import pprint
        # pprint(request)
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Path saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def student_update_api(request, pk):
    # student = get_object_or_404(Student, pk=pk)
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
                "message": f"Student {student.last_name} updated successfully"
            }
        return Response(data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete_api(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    data = {
                "message": f"Student {student.last_name} deleted successfully"
            }
    return Response(data, status=status.HTTP_202_ACCEPTED)
    

@api_view(['PATCH'])
def student_partial_udate(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'message': 'Updated!!!!!!'
        }
        return Response(data)
    data = {
            'message': 'Something wrong!!!'
        }
    return Response(serializer.errors)