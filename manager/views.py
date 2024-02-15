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
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Category.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    serializer_class = serializers.CategorySerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

class CategoriesRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Category.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    serializer_class = serializers.CategorySerializer

# A view to list create update retrieve and delete an account
class Accounts(ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Account.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    serializer_class = serializers.AccountSerializer

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
# Aview to do all actions except the update action on transaction model
class TransactionListCreateView(ListCreateAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Transaction.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    serializer_class = serializers.TransactionSerializer

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

class TransactionsRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Transaction.objects.filter(user_id=self.request.user.id)
        else:
            raise PermissionDenied
    serializer_class = serializers.TransactionSerializer