from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        # return super(UserProfileManager, self).get_queryset().filter(city='London')
        return super(UserProfileManager, self).get_queryset()


class UserProfile(models.Model):
    CUISINE_CHOICES = (
        ('american', 'American'),
        ('asian', 'Asian'),
        ('italian', 'Italian'),
        (None, 'Still tasting!'),
    )
    
    DINING_CHOICES = (
        ('weekly', 'Once a week'),
        ('multi_weekly', 'Couple times a week'),
        ('monthly', 'Once a month'),
        ('multi_monthly', 'Couple times a month'),
        (None, 'Still deciding!'),
    )

    AMBIENCE_CHOICES = (
        ('bustling', 'Bustling'),
        ('calm', 'Calm'),
        ('gastro', 'Gastro-pub feel'),
        ('fine_dining', 'Fine Dining'),
        ('casual', 'Casual'),
        (None, 'Still deciding!'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    fav_cuisine = models.CharField(max_length=20, blank=True, choices=CUISINE_CHOICES, default='american')
    dining_pref = models.CharField(max_length=25, blank=True, choices=DINING_CHOICES, default='monthly')
    ambience = models.CharField(max_length=25, blank=True, choices=AMBIENCE_CHOICES, default='calm')
    unfav_cuisine = models.CharField(max_length=20, blank=True, choices=CUISINE_CHOICES, default='american')

    # Uncomment would filter the User Profiles in Admin
    # london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
