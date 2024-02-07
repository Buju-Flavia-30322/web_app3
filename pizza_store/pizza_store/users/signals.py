from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Activation
from users.views.activation import send_activation_email
from django.db import transaction

AuthUserModel = get_user_model()





@receiver(pre_save,sender=AuthUserModel)
def inactivate_user(sender,instance,**kwargs):
    print('!!! Signal pre_save triggered')
    if not instance.pk:
        instance.is_active=False
        instance.password = None

 # daca cv se petrece in functie exceptie, tot ce s a creat se va sterge di db
@receiver(post_save,sender=AuthUserModel)
def create_activation(sender,instance,created,**kwargs):
    print('!!! Signal post_save triggered')
    try:  # aici banuiesti ca s ar petrece exceptie
        with transaction.atomic():
            if created:
               Activation(user=instance).save()
               send_activation_email(instance)
    except ValueError:
        AuthUserModel.objects.get(pk=instance.id).delete()