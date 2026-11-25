# Initial migration for the RendezVous application.
import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('Cabinet', '0002_alter_medecin_options_alter_patient_options_and_more'),
    ]
    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField(verbose_name='Date et heure')),
                ('motif', models.TextField(verbose_name='Motif')),
                ('statut', models.CharField(choices=[('En attente', 'En attente'), ('Confirmé', 'Confirmé'), ('Annulé', 'Annulé'), ('Terminé', 'Terminé')], default='En attente', max_length=20)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendez_vous', to='Cabinet.medecin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendez_vous', to='Cabinet.patient')),
            ],
            options={'verbose_name': 'Rendez-vous', 'verbose_name_plural': 'Rendez-vous', 'ordering': ['-date_heure']},
        ),
    ]
