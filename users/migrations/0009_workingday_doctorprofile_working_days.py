# Generated by Django 5.0.4 on 2024-08-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_doctorprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='working_days',
            field=models.ManyToManyField(blank=True, related_name='doctor_profiles', to='users.workingday'),
        ),
    ]
