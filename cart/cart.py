from decimal import Decimal
from storefront.models import Book

CART_SESSION_KEY = "cart"


class Cart:
    """A simple session-backed shopping cart keyed by book id."""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = self.session[CART_SESSION_KEY] = {}
        self.cart = cart

    def add(self, book, quantity=1, replace=False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {"quantity": 0, "price": str(book.price)}
        if replace:
            self.cart[book_id]["quantity"] = quantity
        else:
            self.cart[book_id]["quantity"] += quantity
        self.save()

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        books_map = {str(book.id): book for book in books}
        for book_id, item in self.cart.items():
            book = books_map.get(book_id)
            if not book:
                continue
            price = Decimal(item["price"])
            quantity = item["quantity"]
            yield {
                "book": book,
                "quantity": quantity,
                "price": price,
                "total_price": price * quantity,
            }

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())
