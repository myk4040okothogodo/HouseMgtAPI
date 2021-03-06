# Generated by Django 3.2.11 on 2022-02-04 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HouseMgt_API_building', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='careTaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_caretaker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='building',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
