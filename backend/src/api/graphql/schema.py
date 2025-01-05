import strawberry
from src.api.graphql.resolvers.query import Query
from src.api.graphql.resolvers.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)