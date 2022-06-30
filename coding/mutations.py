from typing_extensions import Required
from urllib import request
import graphene
from graphene_file_upload.scalars import Upload
from .tasks import newprocess
from .redis_insert import freq
from .types import BatchType, ProcessedKeywordsType
from .models import Batch, ProcessedKeywords
from userapi.models import UserProfile


class BatchInput(graphene.InputObjectType):
    id = graphene.ID()
    file = Upload(required=True)
    status = graphene.String(required=True)
    created_on = graphene.DateTime()
    created_user = graphene.String(required=True, name="user")


class BatchMutation(graphene.Mutation):
    class Arguments:
        input = BatchInput(required=True)

    batch = graphene.Field(BatchType)

    @classmethod
    def mutate(cls, root, info, input):
        create_new_batch = Batch(
            status=input.status,
            created_user=UserProfile.objects.get(id=input.created_user),
        )
        create_new_batch.save()
        newprocess.delay(freq, "cholera")
        return BatchMutation(batch=create_new_batch)
