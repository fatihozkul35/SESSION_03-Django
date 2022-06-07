from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = { 'message' : 'logout'}
        return Response(data)