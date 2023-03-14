from django.db import models
from django.contrib.auth.models import User


class Feedbacks(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)
    create_date = models.DateField(auto_now=True)
    text = models.TextField(verbose_name="Текст комментария")
    status = models.BooleanField(default=True)
