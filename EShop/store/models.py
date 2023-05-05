from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    completed = models.BooleanField(default=False)

    

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')

# shreyas
# shreyas

# admin
# zxcvbnm@123