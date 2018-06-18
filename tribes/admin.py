from django.contrib import admin
from tribes.models import Event, Tribe

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'tribe')

    def get_queryset(self, request):
        queryset = super(EventAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-date', 'name')
        return queryset


class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'chieftain', 'created')

    def get_queryset(self, request):
        queryset = super(TribeAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-name', 'chieftain')
        return queryset

admin.site.register(Event, EventAdmin)
admin.site.register(Tribe, TribeAdmin)