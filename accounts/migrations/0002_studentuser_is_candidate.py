# Generated by Django 4.2.6 on 2023-10-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='is_candidate',
            field=models.BooleanField(default=False),
        ),
    ]
