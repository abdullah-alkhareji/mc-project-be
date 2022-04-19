from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer

# for viewing user info
class ModifyDjoserUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['username', 'email']

# for creating a user these fields are needed too
class ModifyDjoserUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['username', 'password', 'email']