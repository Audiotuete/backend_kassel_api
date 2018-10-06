from django.db import models
from django.conf import settings
from django.apps import apps as django_apps


class UserPoll(models.Model):
  poll = models.ForeignKey('app_polls.Poll', on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  success_email = models.EmailField()

  class Meta:
    unique_together = ['user', 'poll']

  def __str__(self):
    return str(self.poll)

 
  def save(self, *args, **kwargs):
    # If UserPoll doesn't already exist create it
    if not UserPoll.objects.filter(poll = self.poll, user = self.user).exists():
      print('Creating a new UserPoll ' + str(self.poll.pk))
      super(UserPoll, self).save(*args, **kwargs)
    # # Create new UserAnswers for every Question in Poll

      Question = django_apps.get_model('app_questions', 'Question')

      print(Question.objects.filter(poll = self.poll))

    #   models_dict = {
    #     'QuestionOpen': 'UserAnswerOpen',
    #     'QuestionYesOrNo': 'UserAnswerYesOrNo',
    #     'QuestionMultiple': 'UserAnswerMultiple',
    #   }

    #   for key_model, value_model in models_dict.items(): 
    
    #     QuestionModel = django_apps.get_model('app_questions', key_model)
    #     UserAnswerModel = django_apps.get_model('app_user_answers', value_model)

    #     questions = QuestionModel.objects.filter(poll = self.currentPoll)
    #     print(questions)
    #     user_answers_list = []

    #     for question in questions:
    #       user_answers_list.append(UserAnswerModel(user = self, poll = self.currentPoll, question = question))
    #     UserAnswerModel.objects.bulk_create(user_answers_list)

    # elif self.check_if_poll_changed(self):

    #   changing_user_answers = UserAnswerModel.objects.filter(user = self)

    #   @atomic
    #   def saves_user_answers(changing_user_answers):
    #     for user_answer in changing_user_answers:
    #       print('Poll for ' + user_answer.__class__.__name__ + ' changed from ' + user_answer.poll.poll_name + ' to ' + self.poll.poll_name)
    #       user_answer.poll = self.poll
    #       user_answer.save()
      
    #   saves_user_answers(changing_user_answers)

    #   super(Question, self).save(*args, **kwargs)

    else:
      print('UserPolls are all in place')