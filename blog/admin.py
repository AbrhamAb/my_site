from django.contrib import admin
from .models import Post, Author, Tag
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'slug')
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name')
    list_filter = ('date', 'tags')
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address')
    search_fields = ('first_name', 'last_name', 'email_address')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)



admin.site.register(Post, postAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
