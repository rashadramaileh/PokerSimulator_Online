# Generated by Django 4.2.3 on 2023-08-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0005_delete_cards1_alter_cards_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='suit',
            field=models.CharField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]
