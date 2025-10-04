from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth import get_user_model
from alx_travel_app.listings.models import Listing, Booking, Review
User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def add_arguments(self, parser):
        
        parser.add_argument(

            '-u',
            '--users',
            type=int,
            help='Number of users to create: (default: 5)',
            default=5
        )
        parser.add_argument(
            '-l',
            '--listings',
            type=int,
            help='Number of listings to create: (default: 10)',
            default=10
        )

        parser.add_argument(
            '-b',
            '--bookings',
            type=int,
            help='Number of bookings to create: (default: 10)',
            default=10
        )
        parser.add_argument(
            '-r',
            '--reviews',
            type=int,
            help='Number of reviews to create: (default: 10)',
            default=10
        )
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        seeder = Seed.seeder()
        User.objects.filter(is_superuser=False).delete()
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        seeder.add_entity(User, kwargs.get('users', 5))
        seeder.add_entity(Listing, kwargs.get('listings', 10))
        seeder.add_entity(Booking, kwargs.get('bookings', 10))
        seeder.add_entity(Review, kwargs.get('reviews', 10))
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))