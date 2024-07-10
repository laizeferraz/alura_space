from django.shortcuts import render

from gallery.models import Pictures

def index(request):
    pictures = Pictures.objects.order_by("published_at").filter(published=True)
    return render(request, 'gallery/index.html', {"cards": pictures})

def image(request, picture_id):
    picture = Pictures.objects.get(id=picture_id) or 404
    return render(request, 'gallery/image.html', {"picture": picture})

def search(request):
    pictures = Pictures.objects.order_by("published_at").filter(published=True)
    if "search" in request.GET:
        keyword = request.GET["search"]
        if keyword:
          pictures = pictures.filter(title__icontains=keyword)
    return render(request, 'gallery/search.html', {"cards": pictures})