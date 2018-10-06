from django.apps import apps as django_apps
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

class Poll(models.Model):

  class Meta:
    indexes = [
        models.Index(fields=['poll_code',]),
    ]
  # challenge = models.ForeignKey('app_challenges.Challenge', default=1, on_delete=models.PROTECT)
  # poll_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True )
  poll_name = models.CharField(("Umfrage-Titel"), max_length=140, unique=True)
  poll_description = models.TextField(("Umfragebeschreibung"), max_length=255)

  push_notifications = models.BooleanField(("Push notfications"), default=True)
  poll_code = models.CharField(("Poll Code"),max_length=7, blank=True, unique=True)
  
  def __str__(self):
    return self.poll_name

  def save(self, *args, **kwargs):
    if self.pk is None:

    # Create Poll with unique poll code
      generated_code = get_random_string(length=7).lower()

      # Check if generated_code already exist in the DB and regenerate if true
      while Poll.objects.filter(poll_code = generated_code):
        generated_code = get_random_string(length=7).lower()

      self.poll_code = generated_code
      super(Poll, self).save(*args, **kwargs)

    else:
      super(Poll, self).save(*args, **kwargs)


