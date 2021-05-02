import graphene

from library.core.schema import Query as BookQuery


class Query(BookQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
