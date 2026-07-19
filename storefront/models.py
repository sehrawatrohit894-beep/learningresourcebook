from django.db import models
from django.urls import reverse


SUBJECT_COLORS = [
    ("indigo", "Indigo"),
    ("marigold", "Marigold"),
    ("forest", "Forest"),
    ("terracotta", "Rosewood"),
    ("slate", "Slate"),
]


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)
    grade_range = models.CharField(max_length=40, blank=True, help_text="e.g. Grade 1-5")
    color = models.CharField(max_length=20, choices=SUBJECT_COLORS, default="indigo")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField("ISBN", max_length=20, blank=True)
    grade = models.CharField(max_length=40, blank=True, help_text="e.g. Class 6")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    mrp = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,
                               help_text="Original price, for showing a discount")
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)
    stock = models.PositiveIntegerField(default=50)
    featured = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("storefront:book_detail", args=[self.slug])

    @property
    def in_stock(self):
        return self.stock > 0

    @property
    def discount_percent(self):
        if self.mrp and self.mrp > self.price:
            return round((self.mrp - self.price) / self.mrp * 100)
        return 0


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=160, blank=True, help_text="School / designation")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'General enquiry'}"
class EBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="ebook_covers/", blank=True, null=True)
    pdf_file = models.FileField(upload_to="ebooks/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title