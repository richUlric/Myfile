from django.db import models
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User


def index(request):
    """View function for home page of site."""


    context = {
      
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class Vehicle(models.Model):
    MAKE_CHOICES = (
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Nissan', 'Nissan')
    )
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.make} {self.model} ({self.license_plate})'


class ParkingSpace(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_taken = models.BooleanField(default=False)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.is_taken:
            return f'Parking space {self.number} - {self.vehicle}'
        return f'Parking space {self.number} - Empty'


class ParkingTicket(models.Model):
    STATUS_CHOICES = (
        ('IN', 'In'),
        ('OUT', 'Out')
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='IN')
    charged = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.vehicle} - {self.check_in_time.strftime("%m/%d/%Y %I:%M %p")}'

# Create your models here.
