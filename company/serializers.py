from rest_framework import serializers
from company.models import Company  # Импорт модели Company, а не Article

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id',)