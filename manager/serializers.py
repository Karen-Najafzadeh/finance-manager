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
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Account.objects.create(user_id=user_id, **validated_data)

class AccountSerializer(ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['id','name','balance']
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Account.objects.create(user_id=user_id, **validated_data)
    
class TransactionSerializer(ModelSerializer):
    account = AccountSerializer()
    category = CategorySerializer()
    class Meta:
        model = models.Transaction
        fields = ['id','value','type','description','date','account','category']
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Transaction.objects.create(user_id=user_id, **validated_data)