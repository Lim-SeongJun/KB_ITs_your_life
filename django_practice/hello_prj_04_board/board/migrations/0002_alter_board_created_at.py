# Generated by Django 3.2.13 on 2022-10-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
