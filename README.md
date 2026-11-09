# Kilele Roasters (Django + Bootstrap 5)
    pip install -r requirements.txt
    python manage.py migrate && python manage.py seed_coffees
    python manage.py createsuperuser   # optional, for /admin/
    python manage.py runserver

## Configuration
Set these for any non-local deployment:
`DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS=yourdomain.com`
