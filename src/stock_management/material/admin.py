from django.contrib import admin

from .models import Material, Inward, Outward

admin.site.register(Material)
admin.site.register(Inward)
admin.site.register(Outward)
