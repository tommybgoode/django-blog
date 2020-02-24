from django.contrib import admin
from .models import PageView
from .models import Post

admin.site.register(Post)


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']


admin.site.register(PageView, PageViewAdmin)
