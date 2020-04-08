from django.contrib import admin
from .models import Pets


@admin.register(Pets)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'sex']

    def __str__(self):
        return self.name

# admin.site.register(Pets, PetAdmin)
