from django.contrib import admin

from blog.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ()

