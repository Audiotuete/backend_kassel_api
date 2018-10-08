from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class UserAnswer(models.Model):
  poll = models.ForeignKey('app_polls.Poll', default=1, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  first_touched = models.DateTimeField(null=True, blank=True)
  last_touched = models.DateTimeField(auto_now=True)
  count_touched = models.PositiveIntegerField(default=0)
  status = models.BooleanField(default=False)

  class Meta:
    abstract = True
    unique_together = ['user', 'question']

  def __str__(self):
    return str(self.question)

class UserAnswerYesOrNo(UserAnswer):
  question = models.ForeignKey('app_questions.QuestionYesOrNo', on_delete=models.CASCADE )
  answer_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(0)])
  answer_note = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerOpen(UserAnswer):
  question = models.ForeignKey('app_questions.QuestionOpen', on_delete=models.CASCADE )
  answer_text = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerMultiple(UserAnswer):
  question = models.ForeignKey('app_questions.QuestionMultiple', on_delete=models.CASCADE )
  answer_choice_key = models.IntegerField(default=-1, validators=[MinValueValidator(-1), MaxValueValidator(3)])
 


