# Generated by Django 4.2.3 on 2023-08-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0019_alter_scoring_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Bug', models.CharField(max_length=500)),
            ],
        ),
    ]
