# Generated by Django 5.1.4 on 2025-01-05 15:14

import pgvector.django.vector
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='embedding',
            field=pgvector.django.vector.VectorField(blank=True, dimensions=1536, null=True),
        ),
    ]
