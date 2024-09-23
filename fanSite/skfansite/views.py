from django.shortcuts import render, get_object_or_404
from .models import Book, Author


# Create your views here.
def home(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    author_list = Author.objects
    context = {'book_list': book_list, 'author_list': author_list}
    return render(request, 'home.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    works = Book.objects.filter
    return render(request, 'author.html', {'author': author})


def search(request, search_term):
    searched_list = Book.objects.filter(title__icontains=search_term)
    return render(request, 'search.html', {'searched_list': searched_list})
