from django.contrib import admin

from .models import Challenge


class ChallengeAdmin(admin.ModelAdmin):
  model = Challenge
  readonly_fields = ['challenge_code',]
  actions = None

  # def has_add_permission(self, request):
  #   return False
  def has_delete_permission(self, request, obj=None):
    return False


admin.site.register(Challenge, ChallengeAdmin)
