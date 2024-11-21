
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'year', 'price', 'status')
    list_filter = ('category', 'author', 'status')
    search_fields = ('title', 'author')
