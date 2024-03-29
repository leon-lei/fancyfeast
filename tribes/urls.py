from django.urls import path
from . import views
from tribes.views import (
    MyEvents, MyTribes, TribeCreate, TribeDetails, TribeDelete, 
    TribeUpdate, EventDelete, EventDetails, EventUpdate, 
)


app_name='tribes'

urlpatterns = [
    path('', MyTribes.as_view(), name='my-tribes'),
    path('<int:pk>/', TribeDetails.as_view(), name='tribe-details'),
    path('<int:pk>/leave/', views.tribe_leave, name='tribe-leave'),
    path('tribe/create/', TribeCreate.as_view(), name='tribe-create'),
    path('tribe/<int:pk>/', TribeUpdate.as_view(), name='tribe-update'),
    path('tribe/<int:pk>/delete/', TribeDelete.as_view(), name='tribe-delete'),
    path('event/create/<int:pk>/', views.event_create_pk, name='event-create-pk'),
    path('event/create/', views.event_create, name='event-create'),
    path('event/<int:pk>/', EventDetails.as_view(), name='event-details'),
    path('event/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('event/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('event/myevents/', MyEvents.as_view(), name='my-events'),
]
