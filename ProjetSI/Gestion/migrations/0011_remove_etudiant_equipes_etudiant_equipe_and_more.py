# Generated by Django 4.0 on 2022-01-24 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0010_remove_equipe_etudiants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='Equipes',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='Equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion.equipe'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='AnnéeEtude',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
    ]