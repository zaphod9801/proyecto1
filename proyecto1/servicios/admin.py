from django.contrib import admin
from .models import servicio

# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ("titulo","contenido","imagen","created","updated")
    search_fields = ("titulo","contenido")
    list_filter = ("created","updated",)
    date_hierarchy = "created"

admin.site.register(servicio,servicioAdmin)