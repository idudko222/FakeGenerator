from rest_framework import serializers
from company.models import Company  # Импорт модели Company, а не Article

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    sector = serializers.ChoiceField(choices=Company.SECTOR_CHOICES)
    inn = serializers.CharField(max_length=12)
    founded_date = serializers.DateField(required=False, allow_null=True)
    localisation = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sector = validated_data.get('sector', instance.sector)
        instance.inn = validated_data.get('inn', instance.inn)
        instance.founded_date = validated_data.get('founded_date', instance.founded_date)
        instance.localisation = validated_data.get('localisation', instance.localisation)
        instance.save()
        return instance