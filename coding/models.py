from django.db import models
from userapi.models import UserProfile

# Create your models here.
class Batch(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    file = models.FileField(upload_to="documents/%Y-%m-%d/%H-%m-%S")
    created_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "batches: {} ".format(self.id)


class ProcessedKeywords(models.Model):
    bag_of_words = models.CharField(max_length=100)
    suggestions = models.TextField(blank=True, null=True)
    file_link = models.CharField(max_length=500)
    batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.batch_number
