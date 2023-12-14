from django.contrib import admin
from . models import MLModel


class DataAdmin(admin.ModelAdmin):
  list_display = ('name', 'matematika', 'bahasa_inggris', 'bahasa_indonesia' , 'keberhasilan')
  
admin.site.register(MLModel, DataAdmin)