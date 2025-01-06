from django.db import models
from pgvector.django import VectorField
from . import services


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(
        dimensions=services.EMBEDDING_DIMENSIONS, blank=True, null=True
    )
    can_delete = models.BooleanField(
        default=False, help_text="Use in Jupyter Notebooks"
    )

    def get_embedding_text_raw(self):
        return self.content

    def save(self, *args, **kwargs):
        self.embedding = services.get_embedding(self.get_embedding_text_raw())
        return super().save(*args, **kwargs)
