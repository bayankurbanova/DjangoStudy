from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Human(models.Model):
    username = models.CharField("Username", unique = True, max_length = 20, null = True )
    email = models.CharField("email", unique = True, max_length =35)
    pas = models.CharField("Password", max_length = 50)
    pas1 = models.CharField("Password1", max_length = 50)

def __str__(self):
   return self.username

class Meta:
    verbose_name  = "Пользователь"
    verbose_name_plural = "Пользователи"

class Create(models.Model):
    task = models.CharField("Task", unique = True, max_length = 50, null = True)

class Meta:
    verbose_name = "Задание"
    verbose_name_plural = "Задания"

#class Card(models.Model):
 #   human_id = models.IntegerField("Айди владельца")

#class Meta:
 #   verbose_name = "Корзина"
  #  verbose_name_plural = "Корзины"

#class Item(models.Model):
 #   name = models.CharField("Наименование товара", max_length = 50)
  #  price = models.IntegerField("Цена товара")
   # card_id = models.IntegerField("Айди товара")
    #avatar = models.ImageField("avatar", upload_to = "avatars")

#def __str__(self):
 #   return self.name

#class Meta:
    #verbose_name = "Товар"
    #verbose_name_plural = "Товары"

