from django.contrib import admin

# Register your models here.
from .models import Products, Textile

admin.site.site_header = "Sales Adminstration"
admin.site.site_title = "Sales Page Admin Area"
admin.site.index_title = "Welcome to the Sales admin area"

admin.site.register(Products)
admin.site.register(Textile)
