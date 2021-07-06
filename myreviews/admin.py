from django.contrib import admin

# Register your models here.
from .models import Myreview

class MyreviewAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','comment','list_date')

admin.site.register(Myreview, MyreviewAdmin)