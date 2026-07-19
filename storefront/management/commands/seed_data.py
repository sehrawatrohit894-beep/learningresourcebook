from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from storefront.models import Book, Category, Testimonial


class Command(BaseCommand):
    help = "Populate the database with sample categories, books, testimonials, and an admin user."

    def handle(self, *args, **options):
        categories_data = [
            ("Mathematics", "mathematics", "Class 1-12", "indigo"),
            ("Science", "science", "Class 1-12", "forest"),
            ("English", "english", "Class 1-12", "slate"),
            ("Hindi", "hindi", "Class 1-10", "terracotta"),
            ("Social Science", "social-science", "Class 6-10", "marigold"),
            ("Pre-Primary", "pre-primary", "Nursery-KG", "forest"),
        ]
        cats = {}
        for i, (name, slug, grade, color) in enumerate(categories_data):
            cat, _ = Category.objects.get_or_create(slug=slug, defaults={
                "name": name, "grade_range": grade, "color": color, "order": i
            })
            cats[slug] = cat

        books_data = [
            ("Numbers & Beyond 6", "numbers-beyond-6", "R. Sharma", "mathematics", "Class 6", 210, 260, True, False),
            ("Numbers & Beyond 8", "numbers-beyond-8", "R. Sharma", "mathematics", "Class 8", 240, 280, False, True),
            ("Explore & Discover: Physics 9", "explore-discover-physics-9", "Anita Verma", "science", "Class 9", 265, 320, True, False),
            ("Explore & Discover: Biology 10", "explore-discover-biology-10", "Dr. K. Nair", "science", "Class 10", 275, None, False, True),
            ("Learn & Grow: English Reader 4", "learn-grow-english-4", "Meera Joseph", "english", "Class 4", 180, 210, True, False),
            ("Learn & Grow: Grammar Book 5", "learn-grow-grammar-5", "Meera Joseph", "english", "Class 5", 190, None, False, False),
            ("Shabd Sagar: Hindi Vyakaran 7", "shabd-sagar-hindi-7", "Suresh Chandra", "hindi", "Class 7", 200, 230, True, False),
            ("Byanjan: Hindi Varnamala", "byanjan-hindi-varnamala", "Suresh Chandra", "hindi", "KG", 150, None, False, True),
            ("Our World: Geography 8", "our-world-geography-8", "Farida Khan", "social-science", "Class 8", 230, 270, True, False),
            ("Bharat Itihas: History 9", "bharat-itihas-history-9", "Farida Khan", "social-science", "Class 9", 245, None, False, False),
            ("Rhymes & Rhythms", "rhymes-and-rhythms", "Little Learners Team", "pre-primary", "Nursery", 140, 160, True, False),
            ("Phonics Fun", "phonics-fun", "Little Learners Team", "pre-primary", "LKG", 145, None, False, True),
        ]
        for title, slug, author, cat_slug, grade, price, mrp, featured, new in books_data:
            Book.objects.get_or_create(slug=slug, defaults={
                "title": title, "author": author, "category": cats[cat_slug], "grade": grade,
                "price": price, "mrp": mrp, "featured": featured, "is_new_arrival": new,
                "stock": 40, "isbn": "978-93-00" + str(abs(hash(slug)) % 100000),
                "description": f"{title} is a curriculum-aligned title for {grade}, "
                               f"built with practising teachers to make classroom learning clear and engaging.",
            })

        testimonials_data = [
            ("BookVerse titles are the most reliable resource we've adopted in years. Teachers plan faster and students grasp concepts sooner.", "Jagdish Hora", "Principal, Panchsheel Public School"),
            ("The workbooks paired with the digital companion have genuinely changed how our teachers approach revision.", "Sarat Chandra", "Academic Head, Doon Public School"),
            ("Our teachers appreciated how thoroughly each topic is covered without feeling overloaded.", "Vikas Sharma", "Coordinator, Northland Public School"),
        ]
        for i, (quote, name, role) in enumerate(testimonials_data):
            Testimonial.objects.get_or_create(name=name, defaults={"quote": quote, "role": role, "order": i})

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@bookverse.example", "admin12345")
            self.stdout.write(self.style.SUCCESS("Created superuser -> username: admin / password: admin12345"))

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {Category.objects.count()} categories, {Book.objects.count()} books, "
            f"{Testimonial.objects.count()} testimonials."
        ))
