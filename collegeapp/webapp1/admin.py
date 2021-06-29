from django.contrib import admin
from .models import youtuber
from django.utils.html import format_html
# Register your models here.
class display(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display=('name','myphoto','topic','important')
    search_fields=('name','topic')
    list_editable=('important',)

admin.site.register(youtuber,display)