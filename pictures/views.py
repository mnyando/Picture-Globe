from django.shortcuts import render, redirect
from .models import Image, Location, Category
from .forms import ImageForm


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'pictures/index.html', {'images': images[::-1], 'locations': locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    locations = Location.get_locations()
    return render(request, 'pictures/location.html', {'location_images': images, 'locations': locations, 'current_location': location})


def search_results(request):
    locations = Location.get_locations()
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'pictures/search_results.html', {"message": message, "images": searched_images, "locations": locations})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'pictures/search_results.html', {"message": message, "locations": locations})


def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category'].strip()
            location_name = form.cleaned_data['location'].strip()

            category, _ = Category.objects.get_or_create(name=category_name)
            location, _ = Location.objects.get_or_create(name=location_name)

            image_instance = Image(
                image=form.cleaned_data['image'],
                name=form.cleaned_data['name'].strip(),
                description=form.cleaned_data['description'].strip(),
                author=form.cleaned_data['author'].strip(),
                category=category,
                location=location
            )
            image_instance.save()
            return redirect('/')
    else:
        form = ImageForm()

    locations = Location.get_locations()
    return render(request, 'pictures/add_image.html', {'form': form, 'locations': locations})
