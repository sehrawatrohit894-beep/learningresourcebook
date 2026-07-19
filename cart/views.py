from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from storefront.models import Book
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get("quantity", 1))
    cart.add(book=book, quantity=quantity)
    messages.success(request, f'"{book.title}" added to your cart.')
    next_url = request.POST.get("next") or "cart:cart_detail"
    return redirect(next_url)


@require_POST
def cart_update(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get("quantity", 1))
    if quantity < 1:
        cart.remove(book)
    else:
        cart.add(book=book, quantity=quantity, replace=True)
    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    messages.info(request, f'"{book.title}" removed from your cart.')
    return redirect("cart:cart_detail")
