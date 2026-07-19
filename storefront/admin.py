from django.contrib import admin
from .models import Category, Book, Testimonial, ContactMessage, EBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "grade_range", "color", "order")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "grade", "price", "mrp", "stock", "featured", "is_new_arrival")
    list_filter = ("category", "featured", "is_new_arrival")
    list_editable = ("price", "stock", "featured", "is_new_arrival")
    search_fields = ("title", "author", "isbn")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at",)

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "uploaded_at")
    list_filter = ("category",)
    search_fields = ("title", "author")
