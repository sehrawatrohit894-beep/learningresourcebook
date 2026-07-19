from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Book, Category, Testimonial, EBook


def home(request):
    categories = Category.objects.all()
    featured_books = Book.objects.filter(featured=True).select_related("category")[:8]
    hero_books = Book.objects.filter(slug__in=[
    "reasoning-workbook-3",
    "i-can-do-it-8",
    "reasoning-workbook-1",
    "i-can-do-it-5",
        ])
    new_arrivals = Book.objects.filter(is_new_arrival=True).select_related("category")[:6]
    testimonials = Testimonial.objects.all()
    return render(request, "storefront/home.html", {
        "categories": categories,
        "featured_books": featured_books,
        "hero_books": hero_books,
        "new_arrivals": new_arrivals,
        "testimonials": testimonials,
    })

def catalogue(request):
    books = Book.objects.select_related("category").all()
    categories = Category.objects.all()

    subject = request.GET.get("subject", "")
    query = request.GET.get("q", "")
    sort = request.GET.get("sort", "")

    if subject:
        books = books.filter(category__slug=subject)
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(grade__icontains=query)
        )
    if sort == "price_asc":
        books = books.order_by("price")
    elif sort == "price_desc":
        books = books.order_by("-price")
    elif sort == "title":
        books = books.order_by("title")

    paginator = Paginator(books, 12)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "storefront/catalogue.html", {
        "page_obj": page_obj,
        "categories": categories,
        "current_subject": subject,
        "query": query,
        "sort": sort,
    })


def book_detail(request, slug):
    book = get_object_or_404(Book.objects.select_related("category"), slug=slug)
    related = Book.objects.filter(category=book.category).exclude(pk=book.pk)[:4]
    return render(request, "storefront/book_detail.html", {"book": book, "related": related})


def about(request):
    return render(request, "storefront/about.html")

def vision(request):
    return render(request, "storefront/vision.html")

def ebooks(request):
    ebook_list = EBook.objects.all()
    return render(request, "storefront/ebooks.html", {"ebook_list": ebook_list})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! Our team will get back to you shortly.")
            return redirect("storefront:contact")
    else:
        form = ContactForm()
    return render(request, "storefront/contact.html", {"form": form})
