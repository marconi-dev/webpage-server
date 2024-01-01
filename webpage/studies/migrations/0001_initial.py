# Generated by Django 5.0 on 2024-01-01 20:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('thought', models.TextField(blank=True, null=True)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('study_type', models.CharField(choices=[('vid', 'Video'), ('ppr', 'Papers'), ('art', 'Artigos'), ('blg', 'Blog Post'), ('col', 'Colaborações'), ('tst', 'Testes Pessoais')])),
                ('study_subject', models.CharField(choices=[('fun', 'For Fun'), ('backend', 'Back-End'), ('cs', 'Computer Science'), ('frontend', 'Front-End'), ('midend', 'Mid-End'), ('career', 'Carreira'), ('community', 'Comunidade'), ('sdev', 'Desenvolvimento de Software')])),
                ('technologies', models.ManyToManyField(to='projects.technology')),
            ],
            options={
                'verbose_name': 'estudo',
                'verbose_name_plural': 'estudos',
                'ordering': ('created_at',),
                'default_related_name': 'studies',
            },
        ),
    ]