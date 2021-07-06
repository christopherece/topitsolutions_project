from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','comment','list_date')

admin.site.register(Review, ReviewAdmin)