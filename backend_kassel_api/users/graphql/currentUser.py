import graphene
from graphql_jwt.decorators import login_required

# Types
from .__types import UserType

# Models
from ..models import User


class CurrentUser(graphene.ObjectType):

  current_user = graphene.Field(UserType)

  @login_required
  def resolve_current_user(self, info, **kwargs):
    
    current_user = info.context.user

    return current_user