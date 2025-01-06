from django.apps import apps
from decouple import config
from sentence_transformers import SentenceTransformer
from pgvector.django import CosineDistance
from django.db.models import F

EMBEDDING_MODEL = config("EMBEDDING_MODEL", default="all-MiniLM-L6-v2")
EMBEDDING_DIMENSIONS = config("EMBEDDING_DIMENSIONS")

model = SentenceTransformer(EMBEDDING_MODEL)


def get_embedding(text):
    return model.encode(text)


def search_posts(query, limit=5):
    query_embedding = model.encode(query)
    Post = apps.get_model(app_label="blog", model_name="Post")

    qs = Post.objects.annotate(
        distance=CosineDistance("embedding", query_embedding),
        similarity=1 - F("distance"),
    ).order_by("distance")[:limit]

    return qs
