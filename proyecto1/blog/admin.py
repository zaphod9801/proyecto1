from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ("titulo","contenido","imagen","created","updated")
    search_fields = ("titulo","contenido")
    list_filter = ("created","updated",)
    date_hierarchy = "created"
    
    
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)
