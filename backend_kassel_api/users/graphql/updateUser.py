import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import UserType

#Models

class UpdateUserMutation(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    email = graphene.String(required=True)

  @login_required
  def mutate(self, info, email):

    current_user = info.context.user
    current_user.email = email

    current_user.save()
      
    return UpdateUserMutation(user=current_user)

class UpdateUser(graphene.ObjectType):
  update_user = UpdateUserMutation.Field()