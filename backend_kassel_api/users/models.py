from django.db import models
from django.urls import reverse
from django.apps import apps as django_apps

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  name = models.CharField(_("Name of User"), max_length=255, blank=True)
  currentPoll = models.ForeignKey('app_polls.Poll', on_delete=models.SET_NULL, null=True)
  # currentChallenge = models.ForeignKey('app_challenges.Challenge', on_delete=models.SET_NULL, null=True, blank=True)

  def get_absolute_url(self):
    return reverse("users:detail", kwargs={"username": self.username})
  
  def __str__(self):
    return self.username

  def save(self, *args, **kwargs):

    # If User doesn't already exist create an (empty) UserPoll.
    if self.pk is None or self.check_if_poll_changed(self):
      super(User, self).save(*args, **kwargs)

      UserPollModel = django_apps.get_model('app_user_polls', 'UserPoll')
      user_poll = UserPollModel(user=self, poll=self.currentPoll)

      user_poll.save()
    else:
      super(User, self).save(*args, **kwargs)

  def check_if_poll_changed(instance, *args, **kwargs):
    pre_save_poll_id = User.objects.get(pk = instance.pk).currentPoll_id
    if pre_save_poll_id == instance.currentPoll_id:
      return False
    else:
      return True


