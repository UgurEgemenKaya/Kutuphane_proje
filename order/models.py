from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm , TextInput
from datetime import datetime, timedelta
from books.models import Product


class Shopcart(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return (self.quantity)


class ShopCartForm(ModelForm):
    class Meta:
        model = Shopcart
        fields =['quantity']


class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Kabul', 'Kabul'),
        ('IadeEdildi', 'IadeEdildi'),
        ('Iptal', 'Iptal'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    teslim_tarih = models.DateTimeField(default=datetime.now() + timedelta(days=15))

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','address','phone','city','country']


class OrderProduct(models.Model):
    STATUS = (
        ('New','New'),
        ('Kabul', 'Kabul'),
        ('IadeEdildi', 'IadeEdildi'),
        ('Iptal', 'Iptal'),
    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    teslim_tarih = models.DateTimeField(default=datetime.now()+timedelta(days=15))

    def __str__(self):
        return self.product.title



