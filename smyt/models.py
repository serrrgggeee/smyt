# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField('Группа товара', max_length=64)
    def __unicode__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="categorys", verbose_name='Группа')
    name = models.CharField('Название товара',  max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    #def save(self, *args, **kwargs):
    #    self.category.categorys.object.count
    def __unicode__(self):
        return self.name, self.price


