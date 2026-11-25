from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class RendezVous(models.Model):
    STATUT_CHOICES = [('En attente','En attente'),('Confirmé','Confirmé'),('Annulé','Annulé'),('Terminé','Terminé')]
    patient = models.ForeignKey('Cabinet.Patient', on_delete=models.CASCADE, related_name='rendez_vous')
    medecin = models.ForeignKey('Cabinet.Medecin', on_delete=models.CASCADE, related_name='rendez_vous')
    date_heure = models.DateTimeField(verbose_name='Date et heure')
    motif = models.TextField(verbose_name='Motif')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='En attente')
    class Meta:
        ordering = ['-date_heure']
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'
    def clean(self):
        if self.date_heure and self.date_heure < timezone.now() and self.statut != 'Terminé':
            raise ValidationError({'date_heure': 'La date du rendez-vous doit être dans le futur.'})
        if self.medecin_id and self.date_heure:
            conflits = RendezVous.objects.filter(medecin=self.medecin, date_heure=self.date_heure).exclude(pk=self.pk).exclude(statut='Annulé')
            if conflits.exists(): raise ValidationError('Ce médecin a déjà un rendez-vous à cette date et heure.')
    def __str__(self):
        return f'{self.patient} — Dr {self.medecin} — {self.date_heure:%d/%m/%Y %H:%M}'
