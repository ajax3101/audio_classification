from django.contrib import admin
from .models import ESC50Metadata

@admin.register(ESC50Metadata)
class ESC50MetadataAdmin(admin.ModelAdmin):
    list_display = ('filename', 'category', 'fold', 'target', 'esc10')
    search_fields = ('filename', 'category')  
    list_filter = ('fold', 'esc10', 'category') 