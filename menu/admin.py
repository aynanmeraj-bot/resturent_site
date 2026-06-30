from django.contrib import admin

# Register your models here.
from django.contrib import admin


# Register your models here.
from .models import Reservation, Contact, Dish
admin.site.register(Reservation)
admin.site.register(Contact)
admin.site.register(Dish)

  