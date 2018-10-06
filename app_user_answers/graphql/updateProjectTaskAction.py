# import graphene
# from graphql_jwt.decorators import login_required

# import datetime

# # Types
# from backend_kassel_api.users.graphql.__types import UserType
# from app_questions.graphql.__types import QuestionActionType
# from app_polls.graphql.__types import PollType

# # Models
# from ..models import UserAnswerAction


# class UpdateUserAnswerActionMutation(graphene.Mutation):
#   # poll = graphene.Field(UserType)
#   question = graphene.Field(QuestionActionType)
#   poll = graphene.Field(PollType)
#   first_touched = graphene.types.datetime.DateTime()
#   last_touched = graphene.types.datetime.DateTime()
#   count_touched = graphene.Int()
#   status = graphene.Boolean()
#   submitted_by = graphene.Field(UserType)
#   # description = graphene.String()
#   action_1 = graphene.String()
#   action_2 = graphene.String()
#   action_3 = graphene.String()
#   pass
  
#   class Arguments:
#     question_id = graphene.ID(required=True)
#     status = graphene.Boolean()
#     # description = graphene.String(required=False)
#     action1 = graphene.String(required=False)
#     action2 = graphene.String(required=False)
#     action3 = graphene.String(required=False)

#   @login_required
#   def mutate(self, info, question_id, status, action1="", action2="", action3=""):
#     current_user = info.context.user
#     poll_id = current_user.currentPoll.id
    
#     open_question = UserAnswerAction.objects.get(question_id=question_id, poll_id=poll_id)
#     if not open_question:
#       raise Exception('Invalid Link!')

#     open_question.count_touched += 1
#     open_question.submitted_by = current_user

#     open_question.action_1 = action1
#     open_question.action_2 = action2
#     open_question.action_3 = action3

#     if action1 and action2 and action3:
#       open_question.status = True
#     else:
#       open_question.status = False      
    
#     if open_question.first_touched == None:
#       open_question.first_touched = datetime.datetime.now()
  

#     open_question.save()

#     return UpdateUserAnswerActionMutation(
#       poll = open_question.poll,
#       status = open_question.status,
#       submitted_by = open_question.submitted_by,
#       question = open_question.question,
#       first_touched = open_question.first_touched,
#       last_touched = open_question.last_touched,
#       count_touched = open_question.count_touched,
#       # description = open_question.description,
#       action_1 = open_question.action_1,
#       action_2 = open_question.action_2,
#       action_3 = open_question.action_3,
#     )

# class UpdateUserAnswerAction(graphene.ObjectType):
#     update_user_answers_action = UpdateUserAnswerActionMutation.Field()

