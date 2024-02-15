from django.db import models
from django.conf import settings
class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits = 6, decimal_places = 2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}'s {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits = 6, decimal_places = 2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s {self.name}"

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
    value = models.DecimalField(max_digits = 6, decimal_places = 2)
    period = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.user}'s {self.name} ({self.type})"

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits = 6, decimal_places = 2)
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

    def __str__(self) -> str:
        return f"{self.user} account = {self.account} type = {self.type}"