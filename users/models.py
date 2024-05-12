from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profile"


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
