# Generated by Django 4.2.4 on 2023-08-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0018_scoring_attempts_scoring_correct_scoring_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoring',
            name='score',
            field=models.FloatField(),
        ),
    ]