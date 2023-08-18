# Generated by Django 4.2.3 on 2023-08-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100)),
                ('card_image', models.CharField(default='https://www.wtcpl.org/wp-content/plugins/wp-media-folder/assets/images/default.png', max_length=500)),
            ],
        ),
    ]
