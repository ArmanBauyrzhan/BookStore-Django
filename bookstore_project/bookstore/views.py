
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    sort_by = request.GET.get('sort_by', 'title')
    if sort_by in ['category', 'author', 'year']:
        books = books.order_by(sort_by)
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookstore/book_detail.html', {'book': book})
