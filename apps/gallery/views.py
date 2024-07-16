from django.shortcuts import redirect, render

from apps.gallery.models import Pictures
from apps.gallery.forms import PictureForm

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

def add_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to add images')
        return redirect('login')
    form = PictureForm

    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added successfully')
            return redirect('index')
        else:
            messages.error(request, 'Error adding image')
            return render(request, 'gallery/add_image.html', {"form": form})
    return render(request, 'gallery/add_image.html', {"form": form})


def edit_image(request, picture_id):
    picture = Pictures.objects.get(id=picture_id)
    form = PictureForm(instance=picture)
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated successfully')
            return redirect('index')
        else:
            messages.error(request, 'Error updating image')
            return render(request, 'gallery/edit_image.html', {'form':form, 'picture_id':picture_id})
    return render(request, 'gallery/edit_image.html', {'form':form, 'picture_id':picture_id})

def delete_image(request, picture_id):
    picture = Pictures.objects.get(id=picture_id)
    picture.delete()
    messages.success(request, 'Image deleted successfully')
    return redirect('index')

def filter(request, category):
    pictures = Pictures.objects.order_by("published_at").filter(published=True, category=category)
    return render(request, 'gallery/index.html', {"cards": pictures})