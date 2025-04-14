from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from company.models import Company
from company.serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = PageNumberPagination()

        result_page = paginator.paginate_queryset(companies, request)
        serializer = CompanySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Company': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)