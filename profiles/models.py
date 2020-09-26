from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_email = models.EmailField(max_length=32, null=True)
    profile_telephone = models.CharField(max_length=20, null=True, blank=True)
    profile_country = models.CharField(max_length=40, null=True, blank=True)
    profile_county = models.CharField(max_length=40, null=True, blank=True)
    profile_address_1 = models.CharField(max_length=300, null=True, blank=True)
    profile_address_2 = models.CharField(max_length=300, null=True, blank=True)


def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):

    if created:
        UserPage.objects.create(user=instance)
        instance.userprofile.save()
