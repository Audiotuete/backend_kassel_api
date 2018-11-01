import graphene
from django.apps import apps as django_apps

#Types
from .__types import UserType

#Models
from ..models import User


class CreateUserMutation(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    username = graphene.String(required=True)
    # email = graphene.String(required=True)
    password = graphene.String(required=True)
    pollId = graphene.ID(required=True)

  def mutate(self, info, username, password, pollId):

    username_lowercase = username.lower()

    if len(username) < 3:
      raise Exception('Username must have at least 3 characters!')
    if len(password) < 8:
      raise Exception('The password must be at least 8 characters long!')
    if User.objects.filter(username = username_lowercase):
      raise Exception('Username already exists!')

    Poll = django_apps.get_model('app_polls', 'Poll')
    match_poll = Poll.objects.get(id = pollId) 

    user = User(
      username = username,
      # email = email,
      currentPoll = match_poll
    )
    user.set_password(password)
    user.save()

    return CreateUserMutation(user=user)

class CreateUser(graphene.ObjectType):
  create_user = CreateUserMutation.Field()