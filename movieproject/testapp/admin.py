from django.contrib import admin
from testapp.models import movie

# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display=['ReleaseDate','MovieName','Hero','Heroine','Rating']

admin.site.register(movie,movieAdmin)
