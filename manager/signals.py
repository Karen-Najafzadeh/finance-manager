from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

@receiver(post_save, sender = models.Transaction)
def say_hello (sender, instance, created, **kwargs):
    """
    this signal is created to add or subtract the value of a created transaction
    to the corresponding account and category of the user.
    """
    if created:
        # getting the account and the category
        account = models.Account.objects.get(id = instance.account.id)
        category = models.Category.objects.get(id = instance.category.id)

        # updating the balance of the account and the category
        if instance.type == 'income':
            account.balance += instance.value
            category.balance += instance.value
        else:
            account.balance -= instance.value
            category.balance -= instance.value
        
        #saving
        account.save()
        category.save()
