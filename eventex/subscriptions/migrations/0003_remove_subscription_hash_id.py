# Generated by Django 3.2.9 on 2022-02-18 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20220218_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='hash_id',
        ),
    ]
