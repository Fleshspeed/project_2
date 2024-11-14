from rest_framework import serializers
from .models import Human

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    roles = serializers.CharField(max_length=255)
    

    
