from django.contrib import admin
from .models import Fruit,Vegetable,BestSell
from import_export.admin import ImportExportModelAdmin

@admin.register(Fruit)
class FruitAdmin(ImportExportModelAdmin):
    list_display = ('id','title','information','price')
    search_fields = ('id', 'title')


@admin.register(Vegetable)
class VegetableAdmin(ImportExportModelAdmin):
    list_display = ('id','title','information','price')
    list_display_links = ('id','title','information','price')
    search_fields = ('id','title')


@admin.register(BestSell)
class BestSellAdmin(ImportExportModelAdmin):
    list_display = ('id','title','rating','price')
    list_display_links = ('id','title','rating','price')
    search_fields = ('id','title')

