from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import UserPoll

class UserPollAdmin(ImportExportModelAdmin):
  model = UserPoll
  list_display = ['user', 'poll', 'success_email']
  # actions = None

  def has_add_permission(self, request):
    return False
  # def has_delete_permission(self, request, obj=None):
  #   return False

admin.site.register(UserPoll, UserPollAdmin)