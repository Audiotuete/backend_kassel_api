import graphene
from django.apps import apps as django_apps
from django.utils.crypto import get_random_string
from django.conf import settings
#Types
from .__types import UserType

#Models
from ..models import User


class CreateUserMutation(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    # username = graphene.String(required=True)
    # email = graphene.String(required=True)
    # password = graphene.String(required=True)
    pollId = graphene.ID(required=True)
    browserInfo = graphene.String(required=True)
    osInfo = graphene.String(required=True)


  def mutate(self, info, pollId, browserInfo, osInfo):

    # if len(username) < 3:
    #   raise Exception('Username must have at least 3 characters!')
    # if len(password) < 8:
    #   raise Exception('The password must be at least 8 characters long!')
    # if User.objects.filter(username = username_lowercase):
    #   raise Exception('Username already exists!')

    generated_username = get_random_string(length=16).lower()
      
    while User.objects.filter(username = generated_username):
      generated_username = get_random_string(length=16).lower()

    Poll = django_apps.get_model('app_polls', 'Poll')
    match_poll = Poll.objects.get(id = pollId) 

    user = User(
      username = generated_username,
      # email = email,
      currentPoll = match_poll,
      browserInfo = browserInfo,
      osInfo = osInfo,
    )
    user.set_password(settings.USER_PASSWORD)
    user.save()

    return CreateUserMutation(user=user)

class CreateUser(graphene.ObjectType):
  create_user = CreateUserMutation.Field()