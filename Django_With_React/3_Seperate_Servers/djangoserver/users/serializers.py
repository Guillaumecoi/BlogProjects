from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True) # For confirmation

    class Meta:
        model = UserModel
        fields = ["email", "password", "password2"] 

    def validate(self, data):  # Additional validation
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        if 'email' not in validated_data:
            raise serializers.ValidationError("The email field is required.")
        validated_data['username'] = validated_data['email']
        user = UserModel.objects.create_user(**validated_data)
        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "email"]