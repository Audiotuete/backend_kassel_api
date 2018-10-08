# import graphene
# from graphql_jwt.decorators import login_required

# #Types
# from .__types import UserType

# #Models
# from ..models import User


# class AllUsers(graphene.ObjectType):
#   all_users = graphene.List(UserType)

#   @login_required
#   def resolve_all_users(self, info, **kwargs):
#     return User.objects.all()