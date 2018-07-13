from django.urls import path
from . import views
from tribes.views import (
    MyTribes, TribeCreate, TribeDetails, TribeDelete, TribeUpdate, MyEventsIndex,
    EventCreate, EventDelete, EventDetails, EventUpdate
)


app_name='tribes'

urlpatterns = [
    path('', MyTribes.as_view(), name='my-tribes'),
    path('<int:pk>/', TribeDetails.as_view(), name='tribe-details'),
    path('<int:pk>/leave/', views.tribe_leave, name='tribe-leave'),
    path('tribe/create/', TribeCreate.as_view(), name='tribe-create'),
    path('tribe/<int:pk>/', TribeUpdate.as_view(), name='tribe-update'),
    path('tribe/<int:pk>/delete/', TribeDelete.as_view(), name='tribe-delete'),
    path('event/create/', EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetails.as_view(), name='event-details'),
    path('event/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('event/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('event/myevents/', MyEventsIndex.as_view(), name='my-events-index'),
]
