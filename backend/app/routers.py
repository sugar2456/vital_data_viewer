from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter
import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"
    
    # 新しく追加したフィールド
    @strawberry.field
    def hello_add(self) -> str:
        return "hello add"

@strawberry.type
class Queryw:
    @strawberry.field
    def hellow(self) -> str:
        return "Hellow World"

@strawberry.type
class Mutation:
   @strawberry.mutation
   def change_name(self, name: str) -> str:
       return name + 'change'

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)