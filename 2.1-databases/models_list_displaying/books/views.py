from django.shortcuts import render, redirect

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def books_view_date(request, date=None):
    template = 'books/books_list.html'
    data = Book.objects.all().filter(pub_date=date)
    page = Book.objects.values('pub_date')
    context = {
        'books': data,
        'pages': page,
    }
    return render(request, template, context)

def index_view(request):
    return redirect('books')
