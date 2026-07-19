# BookVerse Publications

A full e-commerce website for an educational book-selling company, built with **Python (Django)**.
Includes a catalogue with subject/category browsing, search & sort, session-based cart, checkout,
user accounts (sign up / login / order history), and a full admin panel to add or edit books, categories,
testimonials, and manage orders.

Design is inspired by educational publisher sites like prachiindia.com — hero banner, subject/category
navigation, featured book grid, services section, and teacher testimonials — reimagined with an original
"subject tab" navigation and a stacked book-spine hero illustration built in pure CSS (no stock images needed).

## Features

- **Catalogue**: browse by subject, search by title/author/class, sort by price or title, pagination
- **Book detail pages** with pricing, discount %, stock, and related titles
- **Cart & checkout**: session-based cart, address form, Cash on Delivery or Online payment method (mocked)
- **Accounts**: sign up, login/logout, order history
- **Admin panel** (Django admin) to add/edit books, categories, testimonials, and manage orders/status
- Fully responsive layout, no external JS framework required

## Requirements

- Python 3.10+
- pip

## Setup

```bash
# 1. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Load sample books, categories, and testimonials (also creates an admin login)
python manage.py seed_data

# 5. Run the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the storefront.

### Admin panel

Visit **http://127.0.0.1:8000/admin/** and log in with:

- username: `admin`
- password: `admin12345`

**Change this password immediately** (Admin panel → Users → admin → change password) before using this
anywhere beyond your own machine. From the admin panel you can:

- Add/edit **Books** (title, author, subject, price, MRP, stock, cover image, featured/new-arrival flags)
- Add/edit **Categories** (subjects), each with a colour used across the site
- Add/edit **Testimonials** shown on the homepage
- View and update **Orders** and their status (pending → confirmed → shipped → delivered)
- Read **Contact messages** submitted through the Contact page

## Project structure

```
bookverse/
├── bookverse/          # project settings & root urls
├── storefront/         # books, categories, home/catalogue/about/contact views
├── cart/                # session-based shopping cart
├── orders/              # checkout, orders, order history
├── accounts/            # sign up / login / logout
├── templates/           # all HTML templates
├── static/css/style.css # design system + all styling
└── manage.py
```

## Notes for going to production

This is a development-ready project. Before deploying publicly:

1. Set `DEBUG = False` in `bookverse/settings.py` and configure `ALLOWED_HOSTS`.
2. Move `SECRET_KEY` to an environment variable.
3. Switch the database from SQLite to Postgres/MySQL for concurrent traffic.
4. Wire up a real payment gateway (e.g. Razorpay/Stripe) in `orders/views.py::checkout` — it currently
   supports Cash on Delivery and a placeholder "Online" option without live payment processing.
5. Serve static/media files via a proper web server or CDN (`collectstatic`).
6. Add real book cover images — books currently use a CSS-generated cover with the subject colour,
   title and author (no image files required), but `Book.cover_image` is ready to accept uploads
   from the admin panel if you'd rather use real artwork.
