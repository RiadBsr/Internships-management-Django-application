# Generated by Django 4.0 on 2022-01-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0016_alter_stage_rapport_delete_rapport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='Rapport',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sujetpfe',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]