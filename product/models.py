from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Orders(models.Model):
    username_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент", blank=True, null=True)
    table = models.DecimalField(max_digits=3, decimal_places=0)
    product_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=6, decimal_places=0)