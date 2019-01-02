from django.db import models
from django.conf import settings
from django.apps import apps as django_apps


class UserPoll(models.Model):
  poll = models.ForeignKey('app_polls.Poll', on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  success_email = models.EmailField()

  class Meta:
    unique_together = ['user', 'poll']

  def __str__(self):
    return str(self.poll)

  def save(self, *args, **kwargs):
    # If UserPoll doesn't already exist create it
    if not UserPoll.objects.filter(user = self.user, poll = self.poll).exists():
      print('Creating a new UserPoll ' + str(self.poll.pk))
      super(UserPoll, self).save(*args, **kwargs)
      
    # # Create new UserAnswers for every Question in Poll

      models_dict = {
        'QuestionOpen': 'UserAnswerOpen',
        'QuestionYesOrNo': 'UserAnswerYesOrNo',
        'QuestionMultiple': 'UserAnswerMultiple',
      }

      for key_model, value_model in models_dict.items():

        UserAnswerModel = django_apps.get_model('app_user_answers', value_model)
        QuestionModel = django_apps.get_model('app_questions', key_model)

        all_questions = QuestionModel.objects.filter(poll = self.poll)

        user_answers_list = []

        for question in all_questions:
            user_answers_list.append(UserAnswerModel(user = self.user, poll = self.poll, question = question))
        UserAnswerModel.objects.bulk_create(user_answers_list)

    else:
      print('UserPolls are all in place')