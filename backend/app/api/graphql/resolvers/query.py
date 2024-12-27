import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str) -> str:
        return f"Hello {name}"
    
    @strawberry.field
    def goodbye(self) -> str:
        return "Goodbye World"