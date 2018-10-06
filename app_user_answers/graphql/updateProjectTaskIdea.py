# import graphene
# from graphql_jwt.decorators import login_required

# import datetime

# # Types
# from backend_kassel_api.users.graphql.__types import UserType
# from app_questions.graphql.__types import QuestionIdeaType
# from app_polls.graphql.__types import PollType

# # Models
# from ..models import UserAnswerIdea


# class UpdateUserAnswerIdeaMutation(graphene.Mutation):
#   # poll = graphene.Field(UserType)
#   question = graphene.Field(QuestionIdeaType)
#   poll = graphene.Field(PollType)
#   first_touched = graphene.types.datetime.DateTime()
#   last_touched = graphene.types.datetime.DateTime()
#   count_touched = graphene.Int()
#   status = graphene.Boolean()
#   submitted_by = graphene.Field(UserType)
#   # description = graphene.String()
#   hashtag_1 = graphene.String()
#   hashtag_2 = graphene.String()
#   hashtag_3 = graphene.String()
#   pass
  
#   class Arguments:
#     question_id = graphene.ID(required=True)
#     status = graphene.Boolean()
#     # description = graphene.String(required=False)
#     hashtag1 = graphene.String(required=False)
#     hashtag2 = graphene.String(required=False)
#     hashtag3 = graphene.String(required=False)

#   @login_required
#   def mutate(self, info, question_id, status, hashtag1="", hashtag2="", hashtag3=""):
#     current_user = info.context.user
#     poll_id = current_user.currentPoll.id
    
#     open_question = UserAnswerIdea.objects.get(question_id=question_id, poll_id=poll_id)
#     if not open_question:
#       raise Exception('Invalid Link!')

#     open_question.submitted_by = current_user

#     open_question.hashtag_1 = hashtag1
#     open_question.hashtag_2 = hashtag2
#     open_question.hashtag_3 = hashtag3

#     if hashtag1 and hashtag2 and hashtag3:
#       open_question.status = True
#     else:
#       open_question.status = False   
    
#     if open_question.first_touched == None:
#       open_question.first_touched = datetime.datetime.now()
#     open_question.count_touched += 1
#     open_question.save()

#     return UpdateUserAnswerIdeaMutation(
#       poll = open_question.poll,
#       status = open_question.status,
#       submitted_by = open_question.submitted_by,
#       question = open_question.question,
#       first_touched = open_question.first_touched,
#       last_touched = open_question.last_touched,
#       count_touched = open_question.count_touched,
#       # description = open_question.description,
#       hashtag_1 = open_question.hashtag_1,
#       hashtag_2 = open_question.hashtag_2,
#       hashtag_3 = open_question.hashtag_3,
#     )

# class UpdateUserAnswerIdea(graphene.ObjectType):
#     update_user_answers_idea = UpdateUserAnswerIdeaMutation.Field()

