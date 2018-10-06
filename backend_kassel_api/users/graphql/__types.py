from graphene_django import DjangoObjectType

#Models
from ..models import User

class UserType(DjangoObjectType):
  class Meta:
    model = User