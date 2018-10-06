from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from app_questions.models import Question, QuestionOpen, QuestionYesOrNo, QuestionMultiple

class QuestionAdmin(OrderedModelAdmin):
  model = Question
  list_display = ('question_type', 'question_text', 'poll', 'move_up_down_links', 'order')
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
  list_display = ('question_text', 'poll',)
  readonly_fields = ['question_type',]

class QuestionYesOrNoAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'poll',)
  readonly_fields = ['question_type',]

class QuestionMultipleAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'poll',)
  readonly_fields = ['question_type',]

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOpen, QuestionOpenAdmin)
admin.site.register(QuestionYesOrNo, QuestionYesOrNoAdmin)
admin.site.register(QuestionMultiple, QuestionMultipleAdmin)
