from django.contrib import admin

# Register your models here.

from .models import Genre, Lang, Type, Status, Year, Season, Episodes, Anime, GenreMap

admin.site.register(Genre)
admin.site.register(Lang)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Year)
admin.site.register(Season)
admin.site.register(Episodes)
admin.site.register(Anime)
admin.site.register(GenreMap)
