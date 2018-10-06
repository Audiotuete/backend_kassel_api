
import graphene
from graphene_django import DjangoObjectType

from ..models import Challenge

class ChallengeType(DjangoObjectType):
  class Meta:
    model = Challenge