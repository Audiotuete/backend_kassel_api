from django.apps import apps as django_apps
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import re
import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import UserType
#Models

class UpdateUserMutation(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    email = graphene.String(required=True)

  @login_required
  def mutate(self, info, email):

    if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
      raise Exception('Email must be a vaild E-Mail-Adress!')

    current_user = info.context.user
    current_user.email = email
    current_user.save()

    UserPoll = django_apps.get_model('app_user_polls', 'UserPoll')
    match_user_poll = UserPoll.objects.get(user = current_user)
    match_user_poll.success_email = email
    match_user_poll.save()

    subject = 'Email Bestätigung für Umfrage Gewinnspiel!'
    html_message = render_to_string('email_confirmation.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    from_email = 'noreply@bewirken.org'
    to = email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    return UpdateUserMutation(user=current_user)

class UpdateUser(graphene.ObjectType):
  update_user = UpdateUserMutation.Field()