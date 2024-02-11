from django.db import models
from django.conf import settings
class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_Model, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    balance = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_Model, on_delete=models.CASCADE)

class AssetLiability(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    asset = 'asset'
    liability = 'liability'
    choices = (
        (asset, 'asset'),
        (liability, 'liability')
    )
    type = models.CharField(choices = choices, max_length=9)
    value = models.DecimalField()
    period = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    value = models.DecimalField()
    income = 'income'
    expence = 'expence'
    choices = (
        (income, 'income'),
        (expence, 'expence')
    )
    type = models.CharField(choices = choices, max_length=7)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)