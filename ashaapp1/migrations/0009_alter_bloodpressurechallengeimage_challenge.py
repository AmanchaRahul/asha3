# Generated by Django 5.1.1 on 2024-09-30 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaapp1', '0008_bloodpressurechallenge_bloodpressurechallengeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressurechallengeimage',
            name='challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloodpressure_images', to='ashaapp1.bloodpressurechallenge'),
        ),
    ]