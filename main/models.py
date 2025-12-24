from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    about = models.TextField(verbose_name="Инфо", blank=True, null=True)
    avatar = models.ImageField(upload_to= "users/", blank = True, null=True)

class initiative(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50, blank=False)
    text = models.TextField(verbose_name="Описание")
    date = models.DateField(auto_now_add=True)
    offering = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "initiatives/", blank=True, null=True)
    adres = models.TextField(default="г.Москва")

    def __str__(self):
        return self.title

class comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    relin = models.ForeignKey(initiative, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий пользователя:{self.author}"

