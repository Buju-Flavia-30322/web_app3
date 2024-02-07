from django.db.models.signals import post_save  # dupa ce salvezi user creezi profil automat
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)  # cand post save a apelat de user se face create prof
def create_profile(sender, instance, created, **kwargs):
    print('!! signal post save was catched')
    if created:
        print('!! we create a profile')
        Profile(user=instance).save()
