from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


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
    lookup_field = 'user__username'

    @action(detail=False, methods=['GET'])
    def compare_users(self, request):
        print(request.query_params)
        username1 = self.request.query_params.get('username1')
        username2 = self.request.query_params.get('username2')
        print(username1, username2)

        if not username1:
            return Response({'error': '"username1" is required.'}, status=400)
        if not username2:
            return Response({'error': '"username2" is required.'}, status=400)


        try:
            user_data1 = my_models.UserData.objects.get(user__username=username1)
        except my_models.UserData.DoesNotExist:
            return Response({'error': f'UserData not found for username1 ({username1}).'}, status=404)
        
        try:
            user_data2 = my_models.UserData.objects.get(user__username=username2)
        except my_models.UserData.DoesNotExist:
            return Response({'error': f'UserData not found for username2 ({username2}).'}, status=404)

        # TODO: Custom comparison logic

        serializer1 = self.get_serializer(user_data1)
        serializer2 = self.get_serializer(user_data2)

        return Response({'user_data1': serializer1.data, 'user_data2': serializer2.data})


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)        
            return Response(data={
                'token': token.key,
                'username': request.data['username'],
                'user_id': user.id,
            })
        else:
            return Response(data={'error': 'invalid data >:('}, status=401)


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

