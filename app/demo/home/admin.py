from django.contrib import admin


from .models import LinkItem


@admin.register(LinkItem)
class LinkItemAdmin(admin.ModelAdmin):
    pass
