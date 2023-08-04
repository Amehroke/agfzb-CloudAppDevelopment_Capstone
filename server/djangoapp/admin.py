from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# Register your models here.

# CarModelInline class
admin.site.register(CarModel)
admin.site.register(CarMake)
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
