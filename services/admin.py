from django.contrib import admin

# Register your models here.
from .models import Webprj

class WebprjAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','comment','list_date','body')

admin.site.register(Webprj, WebprjAdmin)