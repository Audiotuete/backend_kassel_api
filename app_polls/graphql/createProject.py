
from django.apps import apps as django_apps

import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import PollType

#Models
from ..models import Poll

class CreatePollMutation(graphene.Mutation):
  poll = graphene.Field(PollType)

  class Arguments:
    pollName = graphene.String(required=True)
    pollDescription = graphene.String(required=True)

  @login_required
  def mutate(self, info, pollName, pollDescription):
    
    currentUser = info.context.user

    Challenge = django_apps.get_model('app_challenges', 'Challenge')

    poll = Poll(
      poll_name = pollName,
      poll_description = pollDescription,
      poll_creator = currentUser,
      challenge = currentUser.currentChallenge
      )

    poll.save()

    currentUser.currentPoll = poll 
    currentUser.save()

    return CreatePollMutation(
      poll=poll
      )

class CreatePoll(graphene.ObjectType):
  create_poll = CreatePollMutation.Field()