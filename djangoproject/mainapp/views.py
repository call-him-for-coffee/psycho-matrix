from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken

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


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response(data={'token': token.key})
        else:
            return Response(data={'error': 'invalid data >:('}, status=401)


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

