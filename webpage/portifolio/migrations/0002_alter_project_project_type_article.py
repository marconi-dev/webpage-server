# Generated by Django 5.0 on 2023-12-31 16:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('fun', 'For Fun'), ('backend', 'Back-End'), ('cs', 'Computer Science'), ('frontend', 'Front-End'), ('midend', 'Mid-End')]),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article_type', models.CharField(choices=[('fun', 'For Fun'), ('backend', 'Back-End'), ('cs', 'Computer Science'), ('frontend', 'Front-End'), ('midend', 'Mid-End')])),
                ('technologies', models.ManyToManyField(to='portifolio.technology')),
            ],
            options={
                'ordering': ('created_at',),
                'default_related_name': 'articles',
            },
        ),
    ]
