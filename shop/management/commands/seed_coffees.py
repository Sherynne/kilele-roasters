from django.core.management.base import BaseCommand
from shop.models import Coffee

DATA = [
    ("Kangaita", "kangaita", "Kirinyaga", 1650, "Fully washed", "medium", "Blackcurrant, brown sugar, cocoa nib", "Grown on the southern slope of Mt Kenya, picked by cooperative members and dried on raised beds for twelve days.", 1450),
    ("Gatomboya", "gatomboya", "Nyeri", 1780, "Fully washed", "light", "Rhubarb, grapefruit, black tea", "Small-lot SL28 from a cooperative that grades every cherry by hand before the wet mill.", 1650),
    ("Karimikui", "karimikui", "Kiambu", 1560, "Natural", "medium", "Dried mango, red wine, honey", "A sun-dried natural from the Aberdare foothills, turned every two hours to keep the fermentation clean.", 1550),
    ("Kiamabara", "kiamabara", "Embu", 1900, "Fully washed", "light", "Passionfruit, jasmine, lime", "Our highest farm. Cold nights slow the cherry down and concentrate the acidity.", 1850),
    ("Thiriku", "thiriku", "Murang'a", 1700, "Anaerobic", "light", "Lychee, cherry cola, rose", "Sealed-tank fermentation for 72 hours. Loud, sweet and strictly limited.", 1950),
]


class Command(BaseCommand):
    help = "Load the starter coffee catalogue"

    def handle(self, *args, **opts):
        for name, slug, region, elev, process, roast, notes, story, price in DATA:
            Coffee.objects.update_or_create(slug=slug, defaults=dict(
                name=name, region=region, elevation_m=elev, process=process,
                roast=roast, notes=notes, story=story, price_kes=price))
        self.stdout.write(self.style.SUCCESS(f"{len(DATA)} coffees loaded"))
