from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author


def index(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request, "index.html", context)

def index_author(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request, 'index_author.html', context)

def new_book(request):
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'])
    new_book.save()
    return redirect('/')

def new_author(request):
    new_author = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'])
    new_author.save()
    return redirect('/index_author')

def display_book(request, id):
    context = {
        'book_info': Book.objects.get(id=id),
        'all_the_books': Book.objects.all(),
        'author_info': Author.objects.get(id=id),
        'all_the_authors': Author.objects.all(),
    }
    return render(request, 'books.html', context)

def display_author(request, id):
    context = {
        'book_info': Book.objects.get(id=id),
        'author_info': Author.objects.get(id=id),
        'all_the_authors': Author.objects.all(),
        'all_the_books': Book.objects.all(),
    }
    return render(request, 'authors.html', context)

def add_book_to_list(request):
    add_book = Book.objects.create(
        title = Book.objects.get(id=request.POST['title'])
    )
    add_book.save()
    return redirect('/authors.html')

def add_author_to_list(request):
    author_info = Author.objects.get(id=request.POST['author_info'])
    book_info = Book.objects.get(id=request.POST['book_info'])
    book_info.authors.add(author_info)
    return redirect(f'/display_book/{book_info.id}')