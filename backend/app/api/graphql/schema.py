import strawberry
from app.api.graphql.resolvers.query import Query
from app.api.graphql.resolvers.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)