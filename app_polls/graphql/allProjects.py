import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import PollType

#Models
from ..models import Poll

class AllPolls(graphene.ObjectType):
  all_polls = graphene.List(PollType)

  @login_required
  def resolve_all_polls(self, info, **kwargs):
    return Poll.objects.all()

