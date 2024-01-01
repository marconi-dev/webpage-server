# Generated by Django 5.0 on 2024-01-01 20:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('titles', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfil',
            },
        ),
        migrations.CreateModel(
            name='ProfileLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=32)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='my_profile.profile')),
            ],
            options={
                'verbose_name': 'link de perfil',
                'verbose_name_plural': 'links de perfil',
            },
        ),
    ]
