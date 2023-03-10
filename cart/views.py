from django.shortcuts import redirect
from .models import Cart
from catalog.models import Book
from django.views.generic import TemplateView, RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class CartView(RedirectView):
    template_name = ""

    def get(self, request):
        return redirect('catalog.html')

    @method_decorator(login_required)
    def post(self, request):
        book = Book.objects.get(id=request.POST['book_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.add(book)


        return redirect('catalog')


class CartRemove(RedirectView):
    template_name = ""

    def get(self, request):
        return redirect('catalog.html')

    @method_decorator(login_required)
    def post(self, request):
        book = Book.objects.get(id=request.POST['book_id'])
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(book)

        return redirect('catalog')




