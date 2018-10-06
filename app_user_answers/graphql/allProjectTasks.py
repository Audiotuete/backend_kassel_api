import graphene
from itertools import chain
from graphql_jwt.decorators import login_required


# Types
from .__types import BaseUserAnswerType

# Models
from ..models import UserAnswerMultiple, UserAnswerOpen, UserAnswerYesOrNo


class AllUserAnswers(graphene.ObjectType):

  all_user_answers = graphene.List(BaseUserAnswerType)

  @login_required
  def resolve_all_user_answers(self, info, **kwargs):

    challengeId = info.context.user.currentChallenge.id

    pollId = info.context.user.currentPoll.id

    multi_user_answers = UserAnswerMultiple.objects.filter(poll_id = pollId)
    yes_no_user_answers = UserAnswerYesOrNo.objects.filter(poll_id = pollId)
    open_user_answers = UserAnswerOpen.objects.filter(poll_id = pollId)

    all_questions = sorted(
      chain(
        multi_user_answers, 
        yes_no_user_answers,
        open_user_answers,
      ),key=lambda instance: instance.question.order)

    return all_questions