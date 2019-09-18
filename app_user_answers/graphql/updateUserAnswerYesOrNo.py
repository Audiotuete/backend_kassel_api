import graphene
from graphql_jwt.decorators import login_required

import datetime

# Types
from backend_kassel_api.users.graphql.__types import UserType
from app_questions.graphql.__types import QuestionYesOrNoType
from app_polls.graphql.__types import PollType

# Models
from ..models import UserAnswerYesOrNo


class UpdateUserAnswerYesOrNoMutation(graphene.Mutation):
  # poll = graphene.Field(UserType)
  question = graphene.Field(QuestionYesOrNoType)
  poll = graphene.Field(PollType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()

  status = graphene.Boolean()
  answer_value = graphene.Int()
  answer_note = graphene.String()
  
  class Arguments:
    question_id = graphene.ID(required=True)
    answer_value = graphene.Int(required=False)
    answer_note = graphene.String()

  @login_required
  def mutate(self, info, question_id, answer_value, answer_note):
    current_user = info.context.user
    poll_id = current_user.currentPoll.id
    
    try:
      open_answer = UserAnswerYesOrNo.objects.get(user=current_user, question_id=question_id, poll_id = poll_id)
    except:
      raise Exception('Invalid Link! Queried entity does not exist.')

    open_answer.count_touched += 1

    if not answer_note and answer_value == -1:
      open_answer.save()
    else:
      open_answer.answer_note = answer_note

      if answer_note:
        open_answer.answer_value = 2
      elif answer_value > 1  or answer_value < -1:
        raise Exception('Choice not available')
      else: 
        open_answer.answer_value = answer_value

      if answer_value > -1:
        open_answer.status = True
      else:
        open_answer.status = False      
      
      if open_answer.first_touched == None:
        open_answer.first_touched = datetime.datetime.now()

      open_answer.save()

    return UpdateUserAnswerYesOrNoMutation(
      poll = open_answer.poll,
      status = open_answer.status,
      question = open_answer.question,
      first_touched = open_answer.first_touched,
      last_touched = open_answer.last_touched,
      count_touched = open_answer.count_touched,
      answer_value = open_answer.answer_value,
      answer_note = open_answer.answer_note
    )

class UpdateUserAnswerYesOrNo(graphene.ObjectType):
    update_user_answer_yes_or_no = UpdateUserAnswerYesOrNoMutation.Field()

