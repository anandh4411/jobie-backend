# Generated by Django 4.1.7 on 2023-03-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_application_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, upload_to='application-resume'),
        ),
    ]