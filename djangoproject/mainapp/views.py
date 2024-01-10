from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

import mainapp.serializers as my_seriazliers
import mainapp.models as my_models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = my_seriazliers.UserSerializer
    permission_classes = []


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = my_seriazliers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = my_models.UserData.objects.all()
    serializer_class = my_seriazliers.UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]