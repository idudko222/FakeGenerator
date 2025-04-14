from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from company.models import Company
from company.serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({'Companies': serializer.data})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Company': serializer.data}, status=status.HTTP_201_CREATED)
