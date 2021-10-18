# Generated by Django 3.2.8 on 2021-10-14 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sanctuary', '0002_auto_20211014_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reply_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
