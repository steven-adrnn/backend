# api/serializers.py

from rest_framework import serializers
from .models import User, Quiz, QuizProgress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Pastikan password hanya dapat ditulis

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        
class QuizProgressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Tambahkan ini untuk menjadikan user read-only

    class Meta:
        model = QuizProgress
        fields = '__all__'