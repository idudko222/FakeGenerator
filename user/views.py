from django.shortcuts import render
from rest_framework import status
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({'user': serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User': serializer.data}, status=status.HTTP_201_CREATED)
