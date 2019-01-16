from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from backend_kassel_api.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

CUSTOM_USER_FIELDS = (
  (None, {'fields': ('currentPoll',)}),
)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

  form = UserChangeForm
  add_form = UserCreationForm
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('username', 'currentPoll', 'password1', 'password2', ),
    }),
  )
  fieldsets = (('User', {'fields': ('name',)}),) + CUSTOM_USER_FIELDS + auth_admin.UserAdmin.fieldsets
  list_display = ['username', 'currentPoll', 'is_superuser', 'date_joined' ]
  search_fields = ['name',]
