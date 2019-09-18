from django.contrib import admin

from .models import UserAnswerOpen, UserAnswerYesOrNo, UserAnswerMultiple
from import_export.admin import ImportExportModelAdmin


class UserAnswerOpenAdmin(ImportExportModelAdmin):
  model = UserAnswerOpen
  list_display = ['user', 'poll', 'question', 'answer_text', 'status', 'count_touched']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerYesOrNoAdmin(ImportExportModelAdmin):
  model = UserAnswerYesOrNo
  list_display = ['user', 'poll', 'question', 'answer_value', 'answer_note', 'status', 'count_touched']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerMultipleAdmin(ImportExportModelAdmin):
  model = UserAnswerMultiple
  list_display = ['user', 'poll', 'question', 'answer_choice_key', 'status', 'count_touched']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(UserAnswerOpen, UserAnswerOpenAdmin)
admin.site.register(UserAnswerYesOrNo, UserAnswerYesOrNoAdmin)
admin.site.register(UserAnswerMultiple, UserAnswerMultipleAdmin)
