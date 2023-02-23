from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre
from django.db.models import Q
from cart.models import Cart

class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"


    def get(self, request):

        books = Book.objects.all()
        genres = Genre.objects.all()

        try:
            Cart.objects.get(user=request.user)
        except:
            try:
                Cart.objects.create(user=request.user)
            except:
                print("User is anonymous")





        params = {
            "title": "All",
            'books': books,
            'genres': genres

        }
        return render(request, self.template_name, params)

class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)
        genres = Genre.objects.all()

        params = {
            'title': f"{book.title} detail",
            'book': book,
            'genres': genres
        }
        return render(request, self.template_name, params)


class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"
    def get(self, request):
        authors = Author.objects.all()
        genres = Genre.objects.all()

        params = {
            'authors' : authors,
            'genres': genres
        }

        return render(request, self.template_name, params)

class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        genres = Genre.objects.all()

        params = {
            "title": f"{last_name}s",
            "author": author,
            "books": books,
            'genres': genres
        }

        return render(request, self.template_name, params)



class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST['search']
        books_by_title = Book.objects.filter(Q(title__icontains=search) | Q(summary__icontains=search) | Q(price__icontains=search))
        genres = Genre.objects.all()

        params = {
            'books': books_by_title,
            'title': f"{search}",
            'genres': genres
        }

        return render(request, self.template_name, params)


class GenreCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, id):
        genre = Genre.objects.get(id=id)
        books = Book.objects.filter(genre=genre)
        genres = Genre.objects.all()

        params = {

            'title': f"{genre.name}'s",
            'genres': genres,
            'books': books,

        }

        return render(request, self.template_name, params)

class AboutView(TemplateView):
    template_name = "catalog/about.html"

    def get(self, request,):




     return render(request, self.template_name,)