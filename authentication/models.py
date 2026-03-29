# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        default='profile_photos/labosse.png'
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')