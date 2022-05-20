from django.contrib import admin

# Register your models here.
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at', 'rank')


admin.site.register(Review, ReviewAdmin)