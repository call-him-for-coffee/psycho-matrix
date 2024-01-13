from django.contrib.auth.models import Group, User
from rest_framework import serializers
import mainapp.models as my_models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    
    class Meta:
        model = User
        fields = ['url', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = my_models.UserData
        fields = ['user', 'date_of_birth', 'gender', 'favorite_color', 'psychodata']

    def get_psychodata(self, obj):
        return obj.calculate_psychodata()

    psychodata = serializers.SerializerMethodField(method_name=get_psychodata.__name__)

    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
