from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import authentication, permissions
from dunzo.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from dunzo.user_filter import UserFilter



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

