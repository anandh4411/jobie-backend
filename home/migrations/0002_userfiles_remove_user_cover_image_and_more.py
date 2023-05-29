# Generated by Django 4.1.7 on 2023-03-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('profile_image', models.ImageField(upload_to='user-profile')),
                ('cover_image', models.ImageField(upload_to='user-cover')),
                ('resume', models.FileField(upload_to='user-resume')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='resume',
        ),
    ]
