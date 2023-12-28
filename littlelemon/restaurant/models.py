from django.db import models
from django.db import models
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class Booking(models.Model):
    title = models.CharField(max_length = 255)
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits = 10 ,decimal_places = 2)

