# import graphene
# from graphql_jwt.decorators import login_required

# import datetime

# # Types
# from backend_kassel_api.users.graphql.__types import UserType
# from app_questions.graphql.__types import QuestionProblemType
# from app_polls.graphql.__types import PollType

# # Models
# from ..models import UserAnswerProblem


# class UpdateUserAnswerProblemMutation(graphene.Mutation):
#   # poll = graphene.Field(UserType)
#   question = graphene.Field(QuestionProblemType)
#   poll = graphene.Field(PollType)
#   first_touched = graphene.types.datetime.DateTime()
#   last_touched = graphene.types.datetime.DateTime()
#   count_touched = graphene.Int()
#   status = graphene.Boolean()
#   submitted_by = graphene.Field(UserType)
#   # description = graphene.String()
#   keywords = graphene.String()
#   pass
  
#   class Arguments:
#     question_id = graphene.ID(required=True)
#     keywords = graphene.String()

#   @login_required
#   def mutate(self, info, question_id, keywords=""):
#     current_user = info.context.user
#     poll_id = current_user.currentPoll.id
    
#     open_question = UserAnswerProblem.objects.get(question_id=question_id, poll_id=poll_id)
#     if not open_question:
#       raise Exception('Invalid Link!')

#     open_question.keywords = keywords

#     if keywords:
#       open_question.status = True
#     else:
#       open_question.status = False

#     open_question.count_touched += 1
#     open_question.submitted_by = current_user

#     if open_question.first_touched == None:
#       open_question.first_touched = datetime.datetime.now()

#     open_question.save()

#     return UpdateUserAnswerProblemMutation(
#       poll = open_question.poll,
#       status = open_question.status,
#       submitted_by = open_question.submitted_by,
#       question = open_question.question,
#       first_touched = open_question.first_touched,
#       last_touched = open_question.last_touched,
#       count_touched = open_question.count_touched,
#       # description = open_question.description,
#       keywords = open_question.keywords,
#     )

# class UpdateUserAnswerProblem(graphene.ObjectType):
#     update_user_answers_problem = UpdateUserAnswerProblemMutation.Field()

