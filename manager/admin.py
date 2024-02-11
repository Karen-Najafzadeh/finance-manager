from django.contrib import admin
from .models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name','balance','user']
    search_fields = ['user']
    list_editable = ['balance']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','balance','user']
    search_fields = ['user']
    list_editable = ['balance']

@admin.register(AssetLiability)
class AssetLiabilityAdmin(admin.ModelAdmin):
    list_display = ['name','type','user','value','period','account']
    search_fields = ['user']
    list_filter = ['type']
    list_editable = ['value']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['type','user','value','account','category','date']
    search_fields = ['user']
    list_filter = ['type']
    list_editable = ['value']
