from django.shortcuts import redirect, render

from gallery.models import Pictures

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('login')
    
    pictures = Pictures.objects.order_by("published_at").filter(published=True)
    return render(request, 'gallery/index.html', {"cards": pictures})

def image(request, picture_id):
    picture = Pictures.objects.get(id=picture_id) or 404
    return render(request, 'gallery/image.html', {"picture": picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to search for images')
        return redirect('login')
    
    pictures = Pictures.objects.order_by("published_at").filter(published=True)
    if "search" in request.GET:
        keyword = request.GET["search"]
        if keyword:
          pictures = pictures.filter(title__icontains=keyword)
    return render(request, 'gallery/search.html', {"cards": pictures})