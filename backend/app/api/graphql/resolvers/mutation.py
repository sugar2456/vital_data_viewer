import strawberry
from app.api.graphql.resolvers.mutations.fitbit_auth_mutation import FitbitAuthMutation

@strawberry.type
class Mutation(FitbitAuthMutation):
    pass