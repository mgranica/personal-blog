from django.contrib import admin

# Register your models here.
from .models import Home, Subcriber, Contact

admin.site.register(Home)
admin.site.register(Subcriber)
admin.site.register(Contact)