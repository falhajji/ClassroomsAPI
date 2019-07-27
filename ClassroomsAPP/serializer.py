from django.contrib.auth.models import User
from rest_framework import serializers
from classes.models import *

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher']


class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher']


class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     def validate(self, data):
#         my_username = data.get('username')
#         my_password = data.get('password')

#         try:
#             user_obj = User.objects.get(username=my_username)
#         except:
#             raise serializers.ValidationError("This username does not exist, dumbo")

#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination! Pay attention, sweetie.")

#         return data

