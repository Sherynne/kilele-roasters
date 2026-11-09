# Kilele Roasters 

A Django-powered website for **Kilele Roasters**, a fictional specialty Kenyan coffee roastery based in Nairobi.

The site is a custom-designed, responsive storefront built with Django 5 and Bootstrap 5.3. It has a coffee catalogue, a detail page for every coffee, and a contact form that saves enquiries to the database for management in the Django admin.

<!-- Add a screenshot once you have one:
![Kilele Roasters homepage](docs/screenshot.png)
-->

## Features

- Responsive homepage with a custom coffee-inspired design (forest green, gold and cherry red).
- Altitude ridge visualization: every coffee is plotted as a peak by farm elevation, drawn as an animated SVG that links to each coffee.
- Coffee catalogue and individual detail pages (`/coffee/<slug>/`).
- Contact form with server-side validation, CSRF protection and database storage.
- Django admin for managing coffees and customer enquiries.
- Management command that loads a starter catalogue of five Kenyan coffees.
- Environment-based configuration for deployment.
- Bootstrap vendored locally, so styling works without a CDN.
- Accessibility basics: skip link, visible keyboard focus and reduced-motion support.

## Technologies Used

- Python 3.10+
- Django 5
- Bootstrap 5.3 (CSS and JavaScript bundle)
- HTML5 and CSS3, with inline SVG for the altitude visualization
- SQLite
- Google Fonts (Bricolage Grotesque and Newsreader)

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Sherynne/kilele-roasters.git
cd kilele-roasters
```

2. Create and activate a virtual environment:

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Load the starter coffee data:

```bash
python manage.py seed_coffees
```

6. (Optional) Create an administrator account:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

Visit <http://127.0.0.1:8000/> to view the website. The admin panel is at <http://127.0.0.1:8000/admin/>.

## Data Model

| Model | Purpose | Key fields |
|---|---|---|
| `Coffee` | A coffee in the catalogue | name, slug, region, elevation (m), process, roast, tasting notes, story, price per 250 g (KES) |
| `Inquiry` | A message sent through the contact form | name, email, message, created timestamp |

Coffees are ordered by elevation, which is also how they are laid out on the homepage ridge.

## Configuration

For deployment, set the following environment variables:

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Secret key used by Django | Insecure development key |
| `DJANGO_DEBUG` | Set to `0` in production | `1` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of permitted hostnames | `localhost,127.0.0.1` |

Never commit production secrets to GitHub.

## Project Structure

```text
kilele-roasters/
├── config/                 # Django project settings and root URLs
├── shop/
│   ├── management/
│   │   └── commands/       # seed_coffees command
│   ├── migrations/
│   ├── templates/shop/     # base, home and detail templates
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/                # kilele.css (custom design)
│   └── vendor/             # Bootstrap 5.3 CSS and JS
├── manage.py
├── requirements.txt
└── README.md
```

## Roadmap

- Custom 404 page
- Product photography
- Shopping cart and checkout (M-Pesa integration)
- Deployment configuration (WhiteNoise, Gunicorn, PostgreSQL)

## Project Status

A portfolio project demonstrating server-side development with Django, database-backed forms, responsive front-end design and environment-based configuration.

## License

No license has been specified yet. To let others reuse the code, add a `LICENSE` file such as [MIT](https://choosealicense.com/licenses/mit/).
