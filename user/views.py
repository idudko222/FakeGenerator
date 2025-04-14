from django.shortcuts import render
from rest_framework import status
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = PageNumberPagination()

        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
