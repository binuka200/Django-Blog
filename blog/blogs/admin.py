from django.contrib import admin
from .models import Author,Post,Tag,Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("Author","Tag")
    prepopulated_fields = {"Slug":("Title",)}



admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)