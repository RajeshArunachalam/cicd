from coding.models import Batch, ProcessedKeywords
import graphene
from .types import BatchType, ProcessedKeywordsType
from .mutations import BatchMutation, searchPatternMutation
from .redis_insert import freq


class Query(graphene.ObjectType):

    batches = graphene.List(BatchType)
    batch = graphene.Field(BatchType, batch_id=graphene.Int())

    def resolve_batches(self, info, **kwargs):
        return Batch.objects.all().order_by("-id")

    def resolve_batch(self, info, batch_id):
        return Batch.objects.get(pk=batch_id)


class Mutation(graphene.ObjectType):
    create_batch = BatchMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)