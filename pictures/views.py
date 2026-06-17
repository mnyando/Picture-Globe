from django.shortcuts import render
from .models import Image, Location


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
