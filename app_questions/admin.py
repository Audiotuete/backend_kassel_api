from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from app_questions.models import Question, QuestionOpen, QuestionYesOrNo, QuestionMultiple

class QuestionAdmin(OrderedModelAdmin):
  model = Question
  list_display = ('id', 'question_type', 'question_text', 'poll', 'move_up_down_links', 'order')
  readonly_fields = [
          'poll',
          'question_type', 
          # 'question_videolink',
          ]

  def has_add_permission(self, request):
    return False
  # def has_change_permission(self, request, obj=None):
  #   return False


class QuestionOpenAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'poll', 'question_type')
  readonly_fields = ['question_type',]

  def get_form(self, request, obj=None, **kwargs):
    """Override the get_form and extend the 'exclude' keyword arg"""
    if obj:
      kwargs.update({
        'exclude': getattr(kwargs, 'exclude', tuple()) + ('poll', 'question_type'),
      })
    return super(QuestionOpenAdmin, self).get_form(request, obj, **kwargs)

class QuestionYesOrNoAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'poll', 'question_type')
  readonly_fields = ['question_type',]

  def get_form(self, request, obj=None, **kwargs):
    """Override the get_form and extend the 'exclude' keyword arg"""
    if obj:
      kwargs.update({
        'exclude': getattr(kwargs, 'exclude', tuple()) + ('poll', 'question_type'),
      })
    return super(QuestionYesOrNoAdmin, self).get_form(request, obj, **kwargs)

class QuestionMultipleAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'poll', 'question_type')
  readonly_fields = ['question_type',]

  def get_form(self, request, obj=None, **kwargs):
    """Override the get_form and extend the 'exclude' keyword arg"""
    if obj:
      kwargs.update({
        'exclude': getattr(kwargs, 'exclude', tuple()) + ('poll', 'question_type'),
      })
    return super(QuestionMultipleAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOpen, QuestionOpenAdmin)
admin.site.register(QuestionYesOrNo, QuestionYesOrNoAdmin)
admin.site.register(QuestionMultiple, QuestionMultipleAdmin)
