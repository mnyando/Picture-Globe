import os
import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from io import BytesIO
from pictures.models import Category, Location, Image

class Command(BaseCommand):
    help = 'Seeds the database with initial categories, locations, and high-quality images'

    def handle(self, *args, **options):
        self.stdout.write("Cleaning up old data...")
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

        # create locations
        locations_data = ["Tokyo", "Paris", "New York", "Nairobi", "Iceland"]
        locations = {}
        for loc_name in locations_data:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            locations[loc_name] = loc

        # create categories
        categories_data = ["Nature", "Travel", "Architecture", "Food", "People"]
        categories = {}
        for cat_name in categories_data:
            cat, _ = Category.objects.get_or_create(name=cat_name)
            categories[cat_name] = cat

        # images data
        images_data = [
            {
                "url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=800",
                "name": "Shinjuku Street Lights",
                "description": "The neon-lit night streets of Shinjuku, Tokyo, filled with bustling energy and towering skyscrapers.",
                "category": "Travel",
                "location": "Tokyo",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800",
                "name": "Golden Gate of Kyoto",
                "description": "Stunning historic temple architecture surrounded by vibrant autumn maple leaves in Kyoto, Japan.",
                "category": "Architecture",
                "location": "Tokyo",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800",
                "name": "Eiffel Tower View",
                "description": "A classic perspective of the majestic Eiffel Tower rising above the Parisian skyline under a soft morning sky.",
                "category": "Travel",
                "location": "Paris",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=800",
                "name": "Glazed Berry Donut",
                "description": "A delicious, freshly baked donut topped with sweet berry glaze and sprinkles, perfect for a cozy morning breakfast.",
                "category": "Food",
                "location": "Paris",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800",
                "name": "Times Square Crossing",
                "description": "The iconic yellow cabs and brilliant digital billboard displays of Times Square in the heart of Midtown Manhattan.",
                "category": "Architecture",
                "location": "New York",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800",
                "name": "Manhattan Skyline at Dusk",
                "description": "Panoramic view of New York City skyline as twilight settles in, with lights twinkling across Manhattan.",
                "category": "Travel",
                "location": "New York",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800",
                "name": "Serene Camping Night",
                "description": "A small camping tent illuminated from within, sitting peacefully under a wide sky full of stars in the wilderness.",
                "category": "Nature",
                "location": "Iceland",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=800",
                "name": "Sailing into the Sunset",
                "description": "A small wooden boat floating on a crystal-clear lake surrounded by massive mountain ranges during sunset.",
                "category": "Travel",
                "location": "Iceland",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1528164344705-47542687000d?w=800",
                "name": "Mount Fuji Cherry Blossom",
                "description": "Breathtaking scenic view of Mount Fuji crowned with snow, framed by pink cherry blossoms in full bloom.",
                "category": "Nature",
                "location": "Tokyo",
                "author": "Charles"
            },
            {
                "url": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?w=800",
                "name": "Mysterious Pine Forest",
                "description": "Deep in a foggy pine forest where sun rays pierce through the dense canopy, highlighting the mossy forest floor.",
                "category": "Nature",
                "location": "Nairobi",
                "author": "Charles"
            }
        ]

        self.stdout.write("Downloading images and seeding database...")
        for item in images_data:
            try:
                response = requests.get(item["url"], timeout=15)
                if response.status_code == 200:
                    img_temp = BytesIO(response.content)
                    filename = item["name"].lower().replace(" ", "_") + ".jpg"
                    img_instance = Image(
                        name=item["name"],
                        description=item["description"],
                        category=categories[item["category"]],
                        location=locations[item["location"]],
                        author=item["author"]
                    )
                    img_instance.image.save(filename, File(img_temp), save=True)
                    self.stdout.write(self.style.SUCCESS(f"Successfully seeded: {item['name']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error seeding {item['name']}: {e}"))

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))
