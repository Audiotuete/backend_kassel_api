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
  success = graphene.Boolean()

  class Arguments:
    email = graphene.String(required=True)

  @login_required
  def mutate(self, info, email):

    if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
      success = False
      raise Exception('Email must be a vaild E-Mail-Adress!')

    current_user = info.context.user
    current_user.email = email
    current_user.save()

    subject = 'Email-Adresse bestätigen!'
    html_message = render_to_string('email_confirmation.html', {'activation_key': current_user.activation_key})
    plain_message = strip_tags(html_message)
    from_email = 'noreply@bewirken.org'
    to = email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    success = True

    return UpdateUserMutation(success = success)

class UpdateUser(graphene.ObjectType):
  update_user = UpdateUserMutation.Field()