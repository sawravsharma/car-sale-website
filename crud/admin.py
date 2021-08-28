from django.contrib import admin
from .models import Member,Products,User,Cart

# Register your models here.

admin.site.register(Member)
admin.site.register(Products)
admin.site.register(User)
admin.site.register(Cart)
