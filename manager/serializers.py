from rest_framework.serializers import ModelSerializer
from . import models
from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CategorySerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Category
        fields = ['id','balance','balance','user','name']