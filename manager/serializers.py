from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from decimal import Decimal
from . import models



class UserSerializer(ModelSerializer):
    """
    Just a simple serializer class for the overritten User model"""
    class Meta:
        User = get_user_model()
        model = User
        fields = ['username']

class CategorySerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Category
        fields = ['id','balance','balance','user','name']
    
    # here we assign the user id to the newly created category instance, automatically 
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Account.objects.create(user_id=user_id, **validated_data)

class AccountSerializer(ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['id','name','balance']
    
    # here we assign the user id to the newly created account instance, automatically 
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Account.objects.create(user_id=user_id, **validated_data)
    
class TransactionSerializer(ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ['id','value','type','description','date','account','category']
    
    #gets the data from the context dictionary and updates the category and account balance
    def create(self, validated_data):

        #getting the data
        user_id = self.context['user_id']
        account = self.context['account']
        category = self.context['category']
        value = Decimal(self.context['value'])
        transaction_type = self.context['transaction_type']

        #updating account and categoty balance
        if transaction_type == 'income':
            account.balance += value
            category.balance += value
        else :
            account.balance -= value
            category.balance -= value
        account.save()
        category.save()

        #saving the transaction
        return models.Transaction.objects.create(user_id=user_id, **validated_data)