from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fav_cuisine', 'dining_pref', 'ambience', 'unfav_cuisine')

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)
