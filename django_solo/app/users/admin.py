from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        #'picture'
    )
    list_display_links = ('user',)
    list_editable = ('phone_number',)  # 'picture')
    
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created_at',
        'updated_at'
    )

    fieldsets = (
        ('Profile', {
            'fields': ('user',),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created_at', 'updated_at'),)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')


class Profileinline(admin.StackedInline):
    """ Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plurar = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ add profile admin to base user admin """
    
    inlines = (Profileinline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)