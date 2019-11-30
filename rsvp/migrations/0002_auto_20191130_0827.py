# Generated by Django 2.2.7 on 2019-11-30 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='contact',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='reg_no',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
