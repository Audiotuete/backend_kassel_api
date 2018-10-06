import graphene


# Types
from .__types import ChallengeType

# Models
from ..models import Challenge


class AChallenge(graphene.ObjectType):

  a_challenge = graphene.Field(ChallengeType, challengeCode = graphene.String())

  def resolve_a_challenge(self, info, challengeCode, **kwargs):
    
    match_challenge = Challenge.objects.get(challenge_code = challengeCode)

    return match_challenge