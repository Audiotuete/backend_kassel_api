import graphene
from graphql_jwt.decorators import login_required

import datetime

# Types
from backend_kassel_api.users.graphql.__types import UserType
from app_questions.graphql.__types import QuestionOpenType
from app_polls.graphql.__types import PollType

# Models
from ..models import UserAnswerOpen


class UpdateUserAnswerOpenMutation(graphene.Mutation):
  # poll = graphene.Field(UserType)
  question = graphene.Field(QuestionOpenType)
  poll = graphene.Field(PollType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()

  status = graphene.Boolean()
  answer_text = graphene.String()
  pass
  
  class Arguments:
    question_id = graphene.ID(required=True)
    answer_text = graphene.String()

  @login_required
  def mutate(self, info, question_id, answer_text):
    current_user = info.context.user
    poll_id = current_user.currentPoll.id
    
    try:
      open_answer = UserAnswerOpen.objects.get(user=current_user, question_id=question_id, poll_id = poll_id)
    except:
      raise Exception('Invalid Link!')

    open_answer.count_touched += 1

    if answer_text:
      open_answer.answer_text = answer_text
      open_answer.status = True
    elif open_answer.answer_text:
      open_answer.status = True
    else:
      open_answer.status = False      
    
    if open_answer.first_touched == None:
      open_answer.first_touched = datetime.datetime.now()

    open_answer.save()

    return UpdateUserAnswerOpenMutation(
      poll = open_answer.poll,
      status = open_answer.status,
      question = open_answer.question,
      first_touched = open_answer.first_touched,
      last_touched = open_answer.last_touched,
      count_touched = open_answer.count_touched,
      answer_text = open_answer.answer_text
    )

class UpdateUserAnswerOpen(graphene.ObjectType):
    update_user_answer_open = UpdateUserAnswerOpenMutation.Field()

