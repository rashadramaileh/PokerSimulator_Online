# Generated by Django 4.2.3 on 2023-08-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0007_bb_100bb_sb_100bb_utg_100bb'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb_100bb',
            name='action',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sb_100bb',
            name='action',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utg_100bb',
            name='action',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]