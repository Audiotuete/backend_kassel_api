from django.apps import apps as django_apps
from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django.db.transaction import atomic

from ordered_model.models import OrderedModel

class Question(OrderedModel):
  poll = models.ForeignKey('app_polls.Poll', on_delete=models.CASCADE, verbose_name="Poll (not changeable after creation)")
  question_type = models.CharField(max_length=150, default='')
  question_text = models.TextField(max_length=250)
  # question_videolink = models.CharField(max_length=150, null=True, blank=True)
  question_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  __poll_pre_save = None

  order_class_path = __module__ + '.Question'

  class Meta:
    ordering = ('order',)

  def __str__(self):
    return self.question_text

# When Question doesn't already exist create UserAnswer for every user in the poll 
  def save(self, *args, **kwargs):
    question_model_name = self.__class__.__name__

    models_dict = {
      'QuestionOpen': 'UserAnswerOpen',
      'QuestionYesOrNo': 'UserAnswerYesOrNo',
      'QuestionMultiple': 'UserAnswerMultiple',
    }

    # Check if question_model_name is not "Question" to allow ordering inside the Questions Admin
    # Because ordering inside Question Admin sets question_model_name = "Question".
    if question_model_name is 'Question':
      UserAnswerModel = django_apps.get_model('app_user_answers', models_dict['Question' + self.question_type])
    else:
      UserAnswerModel = django_apps.get_model('app_user_answers', models_dict[question_model_name])

    UserPoll = django_apps.get_model('app_user_polls', 'UserPoll')

    if self.pk == None:
      super(Question, self).save(*args, **kwargs)

      all_user_polls = UserPoll.objects.filter(poll = self.poll)

      user_answer_list = []    
      for user_poll in all_user_polls:
        user_answer_list.append(UserAnswerModel(user_id = user_poll.user_id, poll_id = user_poll.poll_id, question = self))
      
      UserAnswerModel.objects.bulk_create(user_answer_list)

    elif not self.poll_changed(self):
      pass
      # changing_user_answers = UserAnswerModel.objects.filter(question = self)

      # @atomic
      # def saves_user_answers(changing_user_answers):
      #   for user_answer in changing_user_answers:
      #     print('Poll for ' + user_answer.__class__.__name__ + ' changed from ' + user_answer.poll.poll_name + ' to ' + self.poll.poll_name)
      #     user_answer.poll = self.poll
      #     user_answer.save()
      
      # saves_user_answers(changing_user_answers)

      # super(Question, self).save(*args, **kwargs)

    else:
      super(Question, self).save(*args, **kwargs)

    if not(self.question_type):
      self.question_type = question_model_name[8:]
      self.save()

  def poll_changed(instance, *args, **kwargs):
    pre_save_poll_id = Question.objects.get(pk = instance.pk).poll_id
    if pre_save_poll_id == instance.poll_id:
      return True
    else:
      return False


# To check if the the question moved to an other poll, we need to save the poll value before save inside "init" and compare it with the current poll.
# See elif above "self.__poll_pre_save is not self.poll"
  # def __init__(self, *args, **kwargs):
  #   super(Question, self).__init__(*args, **kwargs)
  #   self.__poll_id_pre_save = self.poll

class QuestionYesOrNo(Question):
  pass

class QuestionOpen(Question):
  pass

class QuestionMultiple(Question):
  options = ArrayField(models.CharField(max_length=150, blank=True), default=list, null=True, size=6)

 


