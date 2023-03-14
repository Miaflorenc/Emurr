from django.db import models

from django.contrib.auth.models import User


class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент", blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    persons = models.DecimalField(max_digits=2, decimal_places=0)
