from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from accounts.models import User, UserProfile

# Register your models here.


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field not in self.Meta.required:
                self.fields[field].required = False

    class Meta:
        model = UserProfile
        fields = "__all__"
        required = ("first_name", "last_name", "dob")


class AccountsUserAdmin(UserAdmin):
    ordering = ('email',)
    search_fields = ('id', 'guid', 'first_name',
                     'last_name', 'username', 'email')
    list_display = ("id", 'username', 'guid', 'first_name',
                    'last_name', 'email', 'is_staff', 'is_superuser')
    list_filter = ('groups', 'is_superuser',)
    readonly_fields = ('guid',)
    fieldsets = (
        (None, {'fields': ('guid', 'username', 'password',)}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'email', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups')}),
        ('Important dates', {'fields': ('date_joined', 'deleted_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if "first_name" in form.base_fields:
            form.base_fields["first_name"].required = True
        if "image" in form.base_fields:
            form.base_fields["image"].required = False
        return form


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ('id', 'first_name', 'last_name', 'user',
                    "email", 'dob', "gender")
    search_fields = ('id', 'guid', "first_name", "user__contact_number")
    readonly_fields = ("guid", "created")


admin.site.register(User, AccountsUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
