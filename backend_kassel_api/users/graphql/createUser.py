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
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    challengeCode = graphene.String(required=True)

  def mutate(self, info, username, email, password, challengeCode):

    # valitdate Data username, email, password

    Challenge = django_apps.get_model('app_challenges', 'Challenge')
    match_challenge = Challenge.objects.get(challenge_code = challengeCode) 

    user = User(
      username = username,
      email = email,
      currentChallenge = match_challenge
    )
    user.set_password(password)
    user.save()

    return CreateUserMutation(user=user)


class CreateUser(graphene.ObjectType):
  create_user = CreateUserMutation.Field()