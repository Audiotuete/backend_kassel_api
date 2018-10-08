import graphene
from graphql_jwt.decorators import login_required

# Types
from .__types import PollType

# Models
from ..models import Poll


class APoll(graphene.ObjectType):

  a_poll = graphene.Field(PollType, pollCode = graphene.String())
  
  @login_required
  def resolve_a_poll(self, info, pollCode, **kwargs):
    
    match_poll = Poll.objects.get(poll_code = pollCode)

    return match_poll