# Generated by Django 4.2.3 on 2023-08-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerMain', '0015_btn_100bb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='bb_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='btn_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='btn_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cards',
            name='value',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='co_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='co_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='hj_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='hj_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='lj_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='lj_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sb_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sb_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='utg1_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='utg1_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='utg_100bb',
            name='card1',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='utg_100bb',
            name='card2',
            field=models.CharField(max_length=2),
        ),
    ]