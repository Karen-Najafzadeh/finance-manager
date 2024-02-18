from django_filters.rest_framework import FilterSet
from . import models

class TransactionFilter(FilterSet):

    class Meta:
        model = models.Transaction
        fields = {'value':['gt','lt'], 'type':['exact']}

class CategoryFilter(FilterSet):
    class Meta:
        model = models.Category
        fields = {'name':['icontains'], 'balance':['gt','lt']}

class AccountFilter(FilterSet):
    class Meta:
        model = models.Account
        fields = {'name':['icontains'], 'balance':['gt','lt']}

class AssetLiabilityFilter(FilterSet):
    class Meta:
        model = models.AssetLiability
        fields = {'name':['icontains'], 'value':['gt','lt'], 'type':['exact'], 'account':['exact']}