from decimal import Decimal
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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
    # account = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    class Meta:
        model = models.Transaction
        fields = ['id','value','type','description','date','account','category']
    
    def create(self, validated_data):
        #print(f"this is self.context\n{self.context}\n\n")
        user_id = self.context['user_id']
        account = self.context['account']
        category = self.context['category']
        value = Decimal(self.context['value'])
        transaction_type = self.context['transaction_type']
        if transaction_type == 'income':
            account.balance += value
            category.balance += value
        else :
            account.balance -= value
            category.balance -= value
        account.save()
        category.save()
        return models.Transaction.objects.create(user_id=user_id, **validated_data)