import graphene
from graphene_django import DjangoObjectType

#Models
from ..models import Poll

class PollType(DjangoObjectType):
  class Meta:
    model = Poll