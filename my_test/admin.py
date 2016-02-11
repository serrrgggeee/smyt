from django.contrib import admin

from .models import Test, Count
admin.site.register(Test)
admin.site.register(Count)