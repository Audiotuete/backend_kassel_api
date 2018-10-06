import graphene
from graphql_jwt.decorators import login_required
from itertools import chain

#Types
from .__types import BaseQuestionType

#Models
from ..models import QuestionMultiple, QuestionOpen, QuestionYesOrNo


class AllQuestions(graphene.ObjectType):
  all_questions = graphene.List(BaseQuestionType)
  
  @login_required
  def resolve_all_questions(self, info, **kwargs):

    multi_questions = QuestionMultiple.objects.all()
    yes_no_questions = QuestionYesOrNo.objects.all()
    open_questions = QuestionOpen.objects.all()

    all_questions = sorted(
      chain(
        multi_questions, 
        yes_no_questions, 
        open_questions
      ),key=lambda instance: instance.order)

    return all_questions

