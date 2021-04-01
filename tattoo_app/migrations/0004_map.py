# Generated by Django 2.2.4 on 2021-03-31 14:02

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo_app', '0003_auto_20210330_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': (17.031645, 51.106715), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', mapbox_location_field.models.AddressAutoHiddenField(map_id='map')),
            ],
        ),
    ]
