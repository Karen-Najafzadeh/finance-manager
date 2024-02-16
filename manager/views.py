from decimal import Decimal
from django.conf import settings
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from . import models
from . import serializers


# The next two views (CategoriesListCreateView and CategoriesRetrieveDestroyAPIView) are ment to do every action except the update atcion.
# As ListCreateAPIView and RetrieveDestroyAPIView can not be used in a single view, I seperated them into these two views.

class CategoriesListCreateView(ListCreateAPIView):
    """
    This is a concrete view which lists and creates category objects, if the user is authenticated.
    it sends the user_id to the serializer so that the serializer can assign the user_id automatically.
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Category.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    serializer_class = serializers.CategorySerializer


class CategoriesRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """
    This is a concrete view which retrieves and deletes category objects, if the user is authenticated.
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Category.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
        
    serializer_class = serializers.CategorySerializer


class Accounts(ModelViewSet):
    """
    A view to list create update retrieve and delete the user's account,
    so the user must be authenticated.
    to create a new account, the user's id is sent to the serializer to assign the id automatically.
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Account.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
        
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    serializer_class = serializers.AccountSerializer


# Like the two category views, we create two separate concrete views for listing, creating,
# retrieving and deleting transactions, the two classes (TransactionListCreateView) and (TransactionsRetrieveDestroyAPIView)
# are dedicated to do so.
class TransactionListCreateView(ListCreateAPIView):
    """
    A view to list and create the transactions of the user, so the user must be authenticated.
    it also send the necessary data to the corresponding serializer class for creating new transactions and updating category and account ballance.
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Transaction.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied

    def get_serializer_context(self):
        account = models.Account.objects.get(id = self.request.data['account'])
        category = models.Category.objects.get(id = self.request.data['category'])
        value = self.request.data['value']
        transaction_type = self.request.data['type']
        return {'user_id':self.request.user.id, 'account':account, 'category':category,'value':value,'transaction_type':transaction_type}
    
    serializer_class = serializers.TransactionSerializer


class TransactionsRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """
    A simple view to retrieve and delete a specified transaction of an authenticated user
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Transaction.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
        
    serializer_class = serializers.TransactionSerializer


class AssetLiability(ModelViewSet):
    """
    A view to create, list, retrieve, update and destroy an asset_liability object.
    """
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.AssetLiability.objects.filter(user_id  = self.request.user.id)
        else:
            raise PermissionDenied
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    serializer_class = serializers.AssetLiabilitySerializer