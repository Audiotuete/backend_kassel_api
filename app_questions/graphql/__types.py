import graphene
from graphene_django import DjangoObjectType

#Models
from ..models import QuestionMultiple, QuestionOpen, QuestionYesOrNo

class BaseQuestionType(graphene.Interface):
  id = graphene.Int()
  order = graphene.Int()
  question_text = graphene.String()

class QuestionMultipleType(DjangoObjectType):
  options = graphene.String()
  class Meta:
    model = QuestionMultiple
    interfaces = [ BaseQuestionType ]

class QuestionOpenType(DjangoObjectType):
  class Meta:
    model = QuestionOpen
    interfaces = [ BaseQuestionType ]

class QuestionYesOrNoType(DjangoObjectType):
  class Meta:
    model = QuestionYesOrNo
    interfaces = [ BaseQuestionType ]