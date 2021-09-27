from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from useraccount.models import UserAccount

from django.utils.translation import ugettext_lazy as _

class UserAccountAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Linked Data'), {'fields': ('root',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'is_staff')
    search_fields = ('username',)

admin.site.register(UserAccount, UserAccountAdmin)