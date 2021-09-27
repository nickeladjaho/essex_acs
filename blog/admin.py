# articles/admin.py
from django.contrib import admin

from .models import Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}  # new


admin.site.register(Post)
admin.site.register(Author)
