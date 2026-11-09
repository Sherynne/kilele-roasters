from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import InquiryForm
from .models import Coffee


def ridge_points(coffees, lo=1400, hi=2100):
    """Place each coffee on an SVG ridge line: x by rank, y by elevation."""
    n = len(coffees)
    pts = []
    for i, c in enumerate(coffees):
        x = 90 + i * (820 / max(n - 1, 1))
        y = 190 - (c.elevation_m - lo) / (hi - lo) * 150
        pts.append({"coffee": c, "x": round(x), "y": round(y)})
    return pts


def home(request):
    coffees = list(Coffee.objects.all())
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Got it. We reply within one working day.")
            return redirect("/#contact")
    else:
        form = InquiryForm()
    pts = ridge_points(coffees)
    path = " ".join(f"{p['x']},{p['y']}" for p in pts)
    return render(request, "shop/home.html", {"coffees": coffees, "points": pts, "path": path, "form": form})


def coffee_detail(request, slug):
    coffee = get_object_or_404(Coffee, slug=slug)
    return render(request, "shop/detail.html", {"coffee": coffee})
