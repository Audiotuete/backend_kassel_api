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
    pollCode = graphene.String(required=True)
  
  @login_required
  def mutate(self, info, pollCode):
    
    #Find correct Poll inside correct Challenge
    Challenge = django_apps.get_model('app_challenges', 'Challenge')

    theUser = info.context.user
    theChallenge = info.context.user.currentChallenge

    poll_to_join = Poll.objects.get(poll_code = pollCode, challenge = theChallenge)

    #Connect user to poll
    theUser = info.context.user
    theUser.currentPoll = poll_to_join

    theUser.save()

    return JoinPollMutation(poll=poll_to_join)

class JoinPoll(graphene.ObjectType):
  join_poll = JoinPollMutation.Field()