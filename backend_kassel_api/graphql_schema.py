import graphene
import graphql_jwt

from app_questions.graphql.__types import QuestionMultipleType, QuestionOpenType, QuestionYesOrNoType

from backend_kassel_api.users.graphql.currentUser import CurrentUser
# from backend_kassel_api.users.graphql.allUsers import AllUsers
from backend_kassel_api.users.graphql.createUser import CreateUser

from app_challenges.graphql.aChallenge import AChallenge

# from app_polls.graphql.aPoll import APoll
# from app_polls.graphql.allPolls import AllPolls
from app_polls.graphql.joinPoll import JoinPoll
from app_polls.graphql.createPoll import CreatePoll

from app_user_answers.graphql.allUserAnswers import AllUserAnswers

# from app_user_answers.graphql.updateUserAnswerProblem import UpdateUserAnswerProblem
# from app_user_answers.graphql.updateUserAnswerIdea import UpdateUserAnswerIdea
# from app_user_answers.graphql.updateUserAnswerAction import UpdateUserAnswerAction


class Queries(
  CurrentUser,
  AChallenge,
  # APoll,
  # AllUsers,
  # AllPolls,
  AllUserAnswers,
  # AllQuestions,

# -----------------------
  graphene.ObjectType
):
  pass

class Mutations(
  CreateUser,
  CreatePoll,
  JoinPoll,
  # UpdateUserAnswerProblem,
  # UpdateUserAnswerIdea,
  # UpdateUserAnswerAction,
# -----------------------
  graphene.ObjectType
):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(
  query = Queries, 
  types = [
    QuestionMultipleType, 
    QuestionOpenType, 
    QuestionYesOrNoType, 
  ],
  mutation = Mutations)