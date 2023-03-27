from django.db import models

# Create your models here.

class Category(models.Model):
  name=models.CharField(max_length=50,unique=True)
  class Meta:
    ordering=('name',)
  
  def __str__(self):
    return self.name

class Manufacturer(models.Model):
  name=models.CharField(max_length=50,unique=True)
  class Meta:
    ordering=('name',)
  
  def __str__(self) :
    return self.name

class Robot(models.Model):
  category=models.ForeignKey(Category,related_name='robots',on_delete=models.CASCADE)
  manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE,related_name="robots")
  name=models.CharField(max_length=50,unique=True)

  CURRENCY_CHOICES=(('INR','Indian Rupee'),('USD','US Doller'),('EUR','Euro'),)
  currency=models.CharField(max_length=3,choices=CURRENCY_CHOICES,default="INR")
  price=models.IntegerField()
  manufacturing_date=models.DateTimeField()

  class Meta:
    ordering=('name',)
  
  def __str__(self):
    return self.name

