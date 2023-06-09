# Generated by Django 4.1.7 on 2023-04-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=30)),
                ('waiting_time', models.IntegerField()),
                ('lab_courtesy', models.IntegerField()),
                ('querry_response', models.IntegerField()),
                ('lab_reliability', models.IntegerField()),
                ('services_liked', models.TextField()),
                ('services_unliked', models.TextField()),
                ('suggestions', models.TextField()),
            ],
        ),
    ]
