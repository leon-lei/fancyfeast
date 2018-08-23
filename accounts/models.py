from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        # return super(UserProfileManager, self).get_queryset().filter(city='London')
        return super(UserProfileManager, self).get_queryset()


class UserProfile(models.Model):
    CUISINE_CHOICES = (
        ('American', 'American'),
        ('Asian', 'Asian'),
        ('Italian', 'Italian'),
        ('Still tasting!', 'Still tasting!'),
    )
    
    DINING_CHOICES = (
        ('Once a week', 'Once a week'),
        ('Couple times a week', 'Couple times a week'),
        ('Once a month', 'Once a month'),
        ('Couple times a month', 'Couple times a month'),
        ('Still deciding!', 'Still deciding!'),
    )

    AMBIENCE_CHOICES = (
        ('Bustling', 'Bustling'),
        ('Calm', 'Calm'),
        ('Gastro-pub feel', 'Gastro-pub feel'),
        ('Fine Dining', 'Fine Dining'),
        ('Casual', 'Casual'),
        ('Still deciding!', 'Still deciding!'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    fav_cuisine = models.CharField(max_length=20, blank=True, choices=CUISINE_CHOICES, default='American')
    dining_pref = models.CharField(max_length=25, blank=True, choices=DINING_CHOICES, default='Once a month')
    ambience = models.CharField(max_length=25, blank=True, choices=AMBIENCE_CHOICES, default='Calm')
    unfav_cuisine = models.CharField(max_length=20, blank=True, choices=CUISINE_CHOICES, default='American')

    # Uncomment would filter the User Profiles in Admin
    # london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
