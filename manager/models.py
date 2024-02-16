from django.db import models
from django.conf import settings


class Account(models.Model):
    """
    each user can have several accounts, like paypal, visa, personal saving or ...
    """
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits = 6, decimal_places = 2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}'s {self.name}"


class Category(models.Model):
    """
    Every transaction will belong to a category, like sports, car maintainance, transportation and ...
    so that the user can have a good idea of where is their money is being spent.
    """
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits = 6, decimal_places = 2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s {self.name}"


class AssetLiability(models.Model):
    """
    This models shows the assets and liabilities a user has, the object might be an asset and bring in a periodic income,
    or it can be the other way (a liability) and take away your money.
    each asset or liability is linked to an account so at the end of the period (days) it will add or subtrac the value to the account
    """
    
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
    """
    This is a simple models to demonstrate the transactions of a user
    if the type of the transactions is income, the value of the transaction will be added to the linked account and category
    or else, it will subtrac the value from them
    """

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