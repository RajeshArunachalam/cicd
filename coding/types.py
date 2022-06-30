import graphene
from graphene import relay
from django.db.models import fields
from graphene_django.types import DjangoObjectType
from .models import Batch, ProcessedKeywords


class BatchType(DjangoObjectType):
    class Meta:
        model = Batch
        fields = "__all__"
        interfaces = (relay.Node,)


class ProcessedKeywordsType(DjangoObjectType):
    class Meta:
        model = Batch
        fields = "__all__"
        interfaces = (relay.Node,)
