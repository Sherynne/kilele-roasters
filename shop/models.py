from django.db import models
from django.urls import reverse


class Coffee(models.Model):
    class Roast(models.TextChoices):
        LIGHT = "light", "Light"
        MEDIUM = "medium", "Medium"

    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    region = models.CharField(max_length=80)
    elevation_m = models.PositiveIntegerField(help_text="Farm elevation in metres")
    process = models.CharField(max_length=60)
    roast = models.CharField(max_length=10, choices=Roast.choices)
    notes = models.CharField(max_length=160)
    story = models.TextField()
    price_kes = models.PositiveIntegerField(help_text="Price per 250g bag")

    class Meta:
        ordering = ["elevation_m"]
        verbose_name_plural = "coffees"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coffee_detail", args=[self.slug])


class Inquiry(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "inquiries"

    def __str__(self):
        return f"{self.name} ({self.created:%d %b %Y})"
