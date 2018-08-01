import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fancyfeast.settings.dev')

import django
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from tribes.models import Event, Tribe


def populate():
    
    # Create Users
    users = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    for user in users:
        add_user(email=f'{user}@example.com', username=user, password='something', first=user, last='Scott')

    # Create Tribes
    alpha = UserProfile.objects.filter(user=User.objects.get(username='alpha'))[0]
    beta = UserProfile.objects.filter(user=User.objects.get(username='beta'))[0]
    gamma = UserProfile.objects.filter(user=User.objects.get(username='gamma'))[0]
    delta = UserProfile.objects.filter(user=User.objects.get(username='delta'))[0]
    epsilon = UserProfile.objects.filter(user=User.objects.get(username='epsilon'))[0]

    add_tribe(name='cyan', chieftain=alpha, tribespeople=[alpha])
    
    add_tribe(name='magenta', chieftain=alpha, tribespeople=[alpha, beta, gamma])
    
    add_tribe(name='yellow', chieftain=beta, tribespeople=[beta])

    # Create Events
    cyan = Tribe.objects.get(name='cyan')
    magenta = Tribe.objects.get(name='magenta')
    
    add_event(name='breakfast', datetime='2018-01-15 09:00:00', tribe=magenta, going=[alpha, gamma])

    add_event(name='brunch', datetime='2018-04-20 11:00:00', tribe=magenta, going=[alpha])
   
    add_event(name='lunch', datetime='2018-08-10 13:00:00', tribe=magenta, going=[alpha, beta, gamma])
    
    add_event(name='dinner', datetime='2018-08-10 19:00:00', tribe=cyan, going=[alpha])

    add_event(name='munchies', datetime='2018-11-15 23:50:00', tribe=magenta, going=[alpha, beta, gamma])


    # Print out what we have added to the tables
    for u in User.objects.all():
        print(u)

    for t in Tribe.objects.all():
        for e in Event.objects.filter(tribe=t):
            print(f'- {t} - {e}')

def add_user(email, username, password, first, last):
    u = User.objects.get_or_create(email=email, username=username, first_name=first, last_name=last)[0]
    u.set_password(password)
    u.save()
    return u

def add_tribe(name, chieftain, tribespeople=[]):
    t = Tribe.objects.get_or_create(name=name, chieftain=chieftain)[0]
    if len(tribespeople) > 0:
        for tp in tribespeople:
            t.tribesmen.add(tp)
    t.save()
    return t

def add_event(name, datetime, tribe, going=[]):
    e = Event.objects.get_or_create(name=name, datetime=datetime, tribe=tribe)[0]
    if len(going) > 0:
        for g in going:
            e.attendees.add(g)
    e.save()
    return e

# Start execution
if __name__ == '__main__':
    print('Starting FancyFeast population script...')
    populate()