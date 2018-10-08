import graphene
from graphene_django import DjangoObjectType

#Types
from backend_kassel_api.users.graphql.__types import UserType
from app_polls.graphql.__types import PollType
from app_questions.graphql.__types import QuestionMultipleType, QuestionOpenType, QuestionYesOrNoType

#Models
from ..models import UserAnswerMultiple, UserAnswerOpen, UserAnswerYesOrNo

class BaseUserAnswerType(graphene.Interface):
  id = graphene.Int()
  status = graphene.Boolean()
  poll = graphene.Field(PollType)

class UserAnswerMultipleType(DjangoObjectType):
  question = graphene.Field(QuestionMultipleType)
  options = graphene.String()

  class Meta:
    model = UserAnswerMultiple
    interfaces = [ BaseUserAnswerType ]

class UserAnswerOpenType(DjangoObjectType):
  question = graphene.Field(QuestionOpenType)
  class Meta:
    model = UserAnswerOpen
    interfaces = [ BaseUserAnswerType ]

class UserAnswerYesOrNoType(DjangoObjectType):
  question = graphene.Field(QuestionYesOrNoType)
  class Meta:
    model = UserAnswerYesOrNo
    interfaces = [ BaseUserAnswerType ]