from django.db import models

# Create your models here.
class BookingTable(models.Model):
    name = models.CharField(max_length=100,default="Null")
    no_of_guest = models.SmallIntegerField()
    BookingDate = models.DateField()
    def __str__(self):
        return self.name
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    def __str__(self):
        return self.title
    
