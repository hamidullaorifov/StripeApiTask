from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=50,decimal_places=2)
    currency = models.CharField(max_length=20,
    choices=(('usd','$'),('rub','₽')),default='usd'
    )

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    value = models.IntegerField(max_digits=10,decimal_places=2,default=0)
    type = models.CharField(max_length=10,choices=(
        ('percentage','Persentage'),('fixed','Fixed amount')),default='percentage')

class Tax(models.Model):
    value = models.DecimalField(max_digits=10,decimal_places=2,default=0)



class Order(models.Model):
    tax = models.ForeignKey(Tax,on_delete=models.SET_DEFAULT)
    discount = models.ForeignKey(Discount,on_delete=models.SET_DEFAULT)
    def get_total(self):
        total_items_sum = sum([item.get_total_price() for item in self.items.all()])
        if self.discount.type == 'percentage':
            total_price = total_items_sum*(1-self.discount.value/100)
        else:
            total_price = total_items_sum-self.discount.value
        return total_price+self.tax
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_total_price(self):
        return self.item.price*self.quantity
