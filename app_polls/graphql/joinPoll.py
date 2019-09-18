from django.apps import apps as django_apps

import graphene
from graphql_jwt.decorators import login_required


#Types
from .__types import PollType

#Models
from ..models import Poll

class JoinPollMutation(graphene.Mutation):
  poll = graphene.Field(PollType)

  class Arguments:
    pollId = graphene.ID(required=True)
  
  @login_required
  def mutate(self, info, pollId):

    poll_to_join = Poll.objects.get(id = pollId)

    #Connect user to poll
    theUser = info.context.user
    theUser.currentPoll = poll_to_join

    theUser.save()

    return JoinPollMutation(poll=poll_to_join)

class JoinPoll(graphene.ObjectType):
  join_poll = JoinPollMutation.Field()