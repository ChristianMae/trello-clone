# Generated by Django 3.0.2 on 2020-01-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_cardlabel_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardlabel',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
