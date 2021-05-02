import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Book


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("uuid", "created_at", "updated_at", "name")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "uuid": ["exact"],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    book = relay.Node.Field(BookNode)
    all_books = DjangoFilterConnectionField(BookNode)
