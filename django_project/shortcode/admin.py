from django.contrib import admin

from shortcode.models.short_url import URLDefine

class URLDefineAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortened_url', 'is_active']
    readonly_fields = ['created', 'updated']
    fieldsets = (
        ('Main details', {
            'fields': ('url', 'shortened_url', )
        }),
        ('Other properties', {
            'classes': ('collapse',),
            'fields': ('is_active', 'created', 'updated'),
        }),
    )
admin.site.register(URLDefine, URLDefineAdmin)
