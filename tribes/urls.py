from django.urls import path
from tribes.views import IndexView, TribeCreate, TribeDetail, TribeDelete, TribeUpdate
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TribeDetail.as_view(), name='tribe-details'),
    path('tribe/<int:pk>/', TribeUpdate.as_view(), name='tribe-update'),
    path('tribe/<int:pk>/delete/', TribeDelete.as_view(), name='tribe-delete'),
    path('tribe/create/', TribeCreate.as_view(), name='tribe-create'),
]
