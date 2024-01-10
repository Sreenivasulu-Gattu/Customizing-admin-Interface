from django.contrib import admin

from app.models import *

# Register your models here.
class Customizewebpage(admin.ModelAdmin):
    list_display = ['topic_name','name','url','email']
    list_display_links = ['url','name','topic_name']
    # list_editable = ['name','email']  ## It throws an error because !( interSection of (links and editable))
        # That means email should not be in both links and editable
    
    list_editable = ['email']
    list_filter = ['topic_name','name']
    list_per_page = 2
    search_fields = ['name','email']
    
admin.site.register(Topic)

admin.site.register(Webpage,Customizewebpage)

admin.site.register(AccessRecord)

