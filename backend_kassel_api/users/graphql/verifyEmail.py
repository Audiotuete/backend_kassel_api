from django.apps import apps as django_apps
from django.contrib.auth import get_user_model

import graphene
# from graphql_jwt.decorators import login_required

#Types
#Models

class VerifyEmailMutation(graphene.Mutation):
  success = graphene.Boolean()

  class Arguments:
    activation_key = graphene.String(required=True)

  def mutate(self, info, activation_key):
    User = get_user_model()
    pending_user = User.objects.get(activation_key = activation_key)
    if pending_user.email:
      UserPoll = django_apps.get_model('app_user_polls', 'UserPoll')
      match_user_poll = UserPoll.objects.get(user = pending_user)

      match_user_poll.success_email = pending_user.email
      
      match_user_poll.save()
      success = True
    else:
      success = False

    return VerifyEmailMutation(success = success)

class VerifyEmail(graphene.ObjectType):
  verify_email = VerifyEmailMutation.Field()