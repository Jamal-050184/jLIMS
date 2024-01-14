from django.contrib import admin
from .models import Library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
  list_display = ("publisher", "author", "title","pageCount","category","shelfLocation","publishedDate", "isInStock", "dateCheckedOut",)
admin.site.register(Library, LibraryAdmin)