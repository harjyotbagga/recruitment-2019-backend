# Generated by Django 2.2.7 on 2019-11-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('moderator_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=10)),
            ],
        ),
    ]
