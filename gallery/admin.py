from django.contrib import admin

from gallery.models import Pictures

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'font', 'description', 'image', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'font', 'description', 'image')
    list_filter = ('category', 'title', 'user')
    list_editable = ('published',)
    ordering = ('title', 'font', 'description', 'image')
    list_per_page = 10

admin.site.site_header = 'Gallery Admin'
admin.site.site_title = 'Gallery Admin'
admin.site.register(Pictures, PicturesAdmin)
