from django.core import serializers
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Book
# Create your views here.


class Index(ListView):
    """
        this is the view for our homepage
    """
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class StoreBook(ListView):
    """
        this is the view for getting all books and also for storing books
    """
    def get(self, request, *args, **kwargs):
        return redirect("view-book")

    def post(self, request):
        name = request.POST.get('name')
        author = request.POST.get('author')
        language = request.POST.get('language')
        genre = request.POST.get('genre')

        if Book.objects.filter(name=name, author=author, language=language, genre=genre).exists():
            messages.error(request, "This book is already available!")
            return redirect("/")
        else:
            book = Book(name=name, author=author, language=language, genre=genre)
            book.save()

        return redirect("view-book")


class ViewBook(ListView):
    """
        this is the view for getting all books
    """
    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        filt_gen = []
        filt_lang = []
        for item in book:
            try:
                filt_gen.index(item.genre)
            except ValueError:
                filt_gen.append(item.genre)

        for item in book:
            try:
                filt_lang.index(item.language)
            except ValueError:
                filt_lang.append(item.language)

        context = {
            'book': book,
            'filter_gen': filt_gen,
            'filter_lang': filt_lang,
        }
        return render(request, "view-book.html", context)


class Filter(ListView):
    """
        this is the view for filtering books based on some some filter tags
    """
    def get(self, request, *args, **kwargs):
        names = request.GET.getlist('name[]', None)
        output = []
        book = None
        for i in names:
            if Book.objects.filter( Q(language=i) | Q(genre=i) ).exists():
                book = Book.objects.filter(Q(language=i) | Q(genre=i))
                for j in book:
                    output.append(j.id)
        # output = serializers.serialize('json', output)
        return JsonResponse({'book': output}, status=200)


class DetailedView(ListView):
    """
        this is the class for one book's detailed view
    """
    def get(self, request, *args, **kwargs):
        # bk_id = request.GET.get('id', None)
        bk = None
        bk_id = kwargs['id']
        if Book.objects.filter(id=bk_id).exists():
            bk = Book.objects.get(id=bk_id)
        return render(request, "detailed-view.html", {"book": bk})
