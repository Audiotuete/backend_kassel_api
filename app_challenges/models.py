from django.db import models
from django.utils.crypto import get_random_string

import datetime

class Challenge(models.Model):

  class Meta:
    indexes = [
        models.Index(fields=['challenge_code',]),
    ]

  YEAR_CHOICES = [(r,r) for r in range(2018, datetime.date.today().year+2)]

  context = models.CharField(('Kontext (Schule- / Kommune)'), blank=True, max_length=150)
  city = models.CharField(('Stadt'), blank=True, max_length=150)
  year = models.IntegerField(('Jahr'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
  start_date = models.DateField(('Start-Datum'),null=True, blank=True)
  end_date = models.DateField(('End-Datum'),null=True, blank=True)

  challenge_code = models.CharField(('Challenge Code'),max_length=5, blank=True, unique=True)
  
  def __str__(self):
    return self.context

  def save(self, *args, **kwargs):
    # If Challenge doesn't already exist create a new Challenge

    if self.pk is None:
      generated_code = get_random_string(length=5).lower()

# MAKE CHALLENGE CODE UNEDITABLE
      
      while Challenge.objects.filter(challenge_code = generated_code):
        generated_code = get_random_string(length=5).lower()

      self.challenge_code = generated_code

      super(Challenge, self).save(*args, **kwargs)

    # End
    else:    
      super(Challenge, self).save(*args, **kwargs)
