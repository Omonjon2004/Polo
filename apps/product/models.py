from django.db import models
from django.forms import FloatField

from apps.product.choices import (Dress_size_List,
                                  Shoes_size_List,
                                  )
from apps.shared.models import BaseProduct


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bags(BaseProduct):
    name = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='bags_images/')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='bags')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='bags')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='bags')


class Shoes(BaseProduct):
    name = models.CharField(max_length=255, )
    size = models.IntegerField(choices=Shoes_size_List)
    image = models.ImageField(upload_to='shoes_images/')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='shoes')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='shoes')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='shoes')


class Dress(BaseProduct):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=5, choices=Dress_size_List)
    image = models.ImageField(upload_to='dress_images/')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='dress')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='dress')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='dress')


class Jewelry(BaseProduct):
    name = models.CharField(max_length=255, )
    weight = FloatField()
    image = models.ImageField(upload_to='jewelry_images/')
    size = models.DecimalField(max_digits=5, decimal_places=2)
    composition = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      default=None)
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='jewelry')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='jewelry')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='jewelry')


class Jackets(BaseProduct):
    name = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='jackets_images/')
    size = models.CharField(max_length=5, choices=Dress_size_List)
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name="jackets")
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='jackets')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='jackets')


class Electrical(BaseProduct):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='electrical_images/')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='electrical')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='electrical')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='electrical')
