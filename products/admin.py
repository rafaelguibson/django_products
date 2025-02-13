from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # Colunas que serão exibidas no modulo admin
    list_display = ('title', 'category', 'brand', 'price', )
    # Campos que serão considerados para busca
    search_fields = ('title',)
    # Campos que serão considerados para filtros.
    list_filter = ('category', 'brand',)

# Registrar o product admin com o model de product
admin.site.register(models.Product, ProductAdmin)