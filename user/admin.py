from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from .forms import UserCreationForm, UserChangeForm


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the user model.
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',
    )
    list_filter = ('is_staff',)
    search_fields = ('email',)
    ordering = ('email', 'username')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
                                      'username',
                                      'first_name',
                                      'last_name',)}),
        ('Permisions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
            )
        }),
    )
