# Generated by Django 2.2.4 on 2021-03-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='styles',
            name='style_desc',
            field=models.TextField(null=True),
        ),
    ]
