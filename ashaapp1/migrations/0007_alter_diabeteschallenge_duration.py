# Generated by Django 5.1.1 on 2024-09-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaapp1', '0006_diabeteschallenge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabeteschallenge',
            name='duration',
            field=models.IntegerField(choices=[(30, '30 Days'), (60, '60 Days'), (90, '90 Days')]),
        ),
    ]