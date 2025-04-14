from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
