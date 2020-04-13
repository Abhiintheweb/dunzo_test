from rest_framework import serializers
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','first_name','email', 'is_staff']

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','first_name','email', 'is_staff']