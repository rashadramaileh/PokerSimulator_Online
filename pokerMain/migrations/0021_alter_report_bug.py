# Generated by Django 4.2.3 on 2023-08-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0020_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Bug',
            field=models.TextField(max_length=500),
        ),
    ]
