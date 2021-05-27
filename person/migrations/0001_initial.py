# Generated by Django 2.2 on 2021-03-20 04:59

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('firebase_id', models.CharField(max_length=64, unique=True, verbose_name='firebase id')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=240, verbose_name='email')),
                ('email_verified', models.BooleanField(default=False, verbose_name='email verified')),
                ('photo_url', models.URLField(blank=True, null=True, verbose_name='photo url')),
                ('provider_id', models.CharField(max_length=30, verbose_name='provider id')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login at')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'person',
                'ordering': ('created_at',),
            },
        ),
    ]
