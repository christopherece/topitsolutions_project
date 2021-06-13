from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','comment','list_date')

admin.site.register(Blog, BlogAdmin)