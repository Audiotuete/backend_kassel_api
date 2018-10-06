from django.contrib import admin

from .models import Poll

class PollAdmin(admin.ModelAdmin):
  model = Poll
  readonly_fields = ['poll_code',]
  # actions = None

  # def has_add_permission(self, request):
  #   return False
  # def has_delete_permission(self, request, obj=None):
  #   return False

# Register your models here.
admin.site.register(Poll, PollAdmin)
