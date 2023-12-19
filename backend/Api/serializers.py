from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()