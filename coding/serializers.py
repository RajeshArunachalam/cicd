from django.core import serializer
from .models import Batch, ProcessedKeywords


class BatchSerializer(serializer.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"