from django.shortcuts import render
from rest_framework.decorators import APIView
from django.contrib.auth.models import auth
from django.db.models import Q
from reddit_api.models import User

from rest_framework.response import Response
# Create your views here.

class Register(APIView):
    def post(self, request):
        print(request.data)
        username = request.data.get("username")
        print("username: ", username)
        email = request.data.get("email")
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response({"message": "username or email is already in use"})
        password = request.data.get("password")
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return Response({"message":f"User '{user.username}' created."})

class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return Response({"message":f"Welcome, {user.username} "})
        else:
            return Response({"message":"Invalid credentials."})

class Logout(APIView):
    def post(self, request):
        auth.logout(request)
        return Response({'message':'successfully logged out'})

class GetCurrentUser(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({"message":f"Current user is {request.user}"})
        else:
            return Response({"message":f"Not logged in."})