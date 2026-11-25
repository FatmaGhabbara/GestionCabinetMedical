from django import forms
from .models import RendezVous
class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['patient','medecin','date_heure','motif','statut']
        widgets = {'date_heure': forms.DateTimeInput(attrs={'type':'datetime-local'}), 'motif': forms.Textarea(attrs={'rows':3})}
