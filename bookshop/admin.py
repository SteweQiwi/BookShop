from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Shop)
admin.site.register(BookSold)
admin.site.register(Purchase)
admin.site.register(InStock)

# Register your models here.
