from django.contrib import admin

# Register your models here.
from stores.models import Pizzeria, Image

admin.site.register(Pizzeria)
admin.site.register(Image)
