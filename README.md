# Kilele Roasters 

A Django-powered website for **Kilele Roasters**, a fictional specialty Kenyan coffee roastery based in Nairobi.

The site is built on the **Agency** theme from [Start Bootstrap](https://startbootstrap.com/theme/agency) (MIT), converted into a Django project and re-themed for a coffee roaster. Every section of the page (services, coffees, story timeline, team) is driven by database models and editable in the Django admin, and the contact form saves enquiries to the database.

<!-- Add a screenshot once you have one:
![Kilele Roasters homepage](docs/screenshot.png)
-->

## Features

- Real Bootstrap template (Start Bootstrap Agency 7.0.12) converted to Django templates, re-coloured and re-typeset for the brand.
- Altitude ridge in the hero: every coffee is plotted as a peak by farm elevation, drawn as an animated SVG. Clicking a peak opens that coffee's detail modal.
- Coffee grid with detail modals, plus services, story timeline and team sections, all loaded from the database.
- Generated artwork: each coffee gets its own SVG contour map, built by `scripts/generate_art.py`.
- Custom 404 page.
- Automated tests for the homepage, the contact form and the 404 page.
- Contact form with server-side validation, CSRF protection and database storage.
- Django admin for managing coffees and customer enquiries.
- Management command that loads a starter catalogue of five Kenyan coffees.
- Environment-based configuration for deployment.
- Bootstrap and Font Awesome vendored locally. Only Google Fonts load from a CDN.
- Accessibility basics: skip link, visible keyboard focus and reduced-motion support.

## Technologies Used

- Python 3.10+
- Django 5
- Start Bootstrap Agency theme (built on Bootstrap 5.2), with the Bootstrap 5.3 JavaScript bundle
- Font Awesome Free 6
- HTML5 and CSS3, with inline SVG for the altitude visualization
- A small amount of vanilla JavaScript (`static/js/kilele.js`)
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

5. Load the starter content (coffees, services, story and team):

```bash
python manage.py seed_coffees
```

6. (Optional) Run the tests:

```bash
python manage.py test
```

7. (Optional) Create an administrator account:

```bash
python manage.py createsuperuser
```

8. Start the development server:

```bash
python manage.py runserver
```

Visit <http://127.0.0.1:8000/> to view the website. The admin panel is at <http://127.0.0.1:8000/admin/>.

## Data Model

| Model | Purpose | Key fields |
|---|---|---|
| `Service` | Cards in the "What we do" section | title, icon, text, order |
| `TimelineEvent` | Entries in the "Our story" timeline | period, title, text, order |
| `TeamMember` | People in the team section | name, role, order |
| `Coffee` | A coffee in the catalogue | name, slug, region, elevation (m), process, roast, tasting notes, story, price per 250 g (KES) |
| `Inquiry` | A message sent through the contact form | name, email, optional phone, message, created timestamp |

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
│   ├── templates/          # shop/base.html, shop/home.html, 404.html
│   ├── tests.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/                # styles.css (Agency theme, re-coloured) and kilele.css (overrides)
│   ├── js/                 # scripts.js (theme) and kilele.js
│   ├── img/                # generated SVG artwork
│   └── vendor/             # Bootstrap JS bundle and Font Awesome
├── scripts/                # generate_art.py
├── manage.py
├── requirements.txt
└── README.md
```

## Roadmap

- Real product photography and team portraits (the current images are generated placeholders)
- Shopping cart and checkout (M-Pesa integration)
- Deployment configuration (WhiteNoise, Gunicorn, PostgreSQL)

## Credits

- [Start Bootstrap Agency](https://github.com/StartBootstrap/startbootstrap-agency) theme, MIT licensed. Its licence is kept in `LICENSE-startbootstrap-agency.txt`.
- [Font Awesome Free](https://fontawesome.com), licences in `LICENSE-fontawesome-free.txt`.
- Fonts: Bricolage Grotesque and Newsreader via Google Fonts.

## Project Status

A portfolio project demonstrating server-side development with Django, database-backed forms, responsive front-end design and environment-based configuration.

## License

No licence has been specified for the Kilele code yet. Third-party licences are included as noted in Credits. To let others reuse your code, add a `LICENSE` file such as [MIT](https://choosealicense.com/licenses/mit/).
