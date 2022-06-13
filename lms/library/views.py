from django.shortcuts import render, redirect
from .models import Book

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def allbooks(request):
    allbooks = Book.objects.all()
    context = {'books': allbooks}
    return render(request, 'library/home.html', context)


@login_required(login_url='/student/login/')
@user_passes_test(lambda u: u.is_superuser, login_url='/student/login/')
def addbook(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        author = request.POST['author']
        image = request.FILES['book-image']
        if author is not None or author != '':
            newbook, created = Book.objects.get_or_create(name=name, image=image, category=category, author=author)
            messages.success(request, 'Book - {} Added succesfully '.format(newbook.name))
            return render(request, 'library/addbook.html')
        else:
            messages.error(request, 'Author not found !')
            return render(request, 'library/addbook.html')
    else:
        return render(request, 'library/addbook.html')


@login_required(login_url='/student/login/')
@user_passes_test(lambda u: u.is_superuser, login_url='/student/login/')
def deletebook(request, id):
    book = Book.objects.get(id=id)
    messages.success(request, 'Book - {} Deleted succesfully '.format(book.name))
    book.delete()
    return redirect('/')

