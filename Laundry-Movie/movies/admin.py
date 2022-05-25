# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'release_date', 'vote_average', 'poster_path', 'video_path', 'runtime')
admin.site.register(Movie, MovieAdmin)