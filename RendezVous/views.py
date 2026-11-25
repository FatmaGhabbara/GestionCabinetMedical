from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RendezVousForm
from .models import RendezVous
@login_required
def liste_rendezvous(request):
    rendezvous = RendezVous.objects.select_related('patient','medecin').all()
    statut = request.GET.get('statut')
    if statut: rendezvous = rendezvous.filter(statut=statut)
    return render(request,'RendezVous/liste.html',{'rendezvous':rendezvous,'statuts':RendezVous.STATUT_CHOICES,'statut_actuel':statut})
@login_required
def ajouter_rendezvous(request):
    form = RendezVousForm(request.POST or None)
    if form.is_valid():
        form.save(); messages.success(request,'Rendez-vous ajouté avec succès.'); return redirect('liste_rendezvous')
    return render(request,'RendezVous/formulaire.html',{'form':form,'titre':'Ajouter un rendez-vous'})
@login_required
def modifier_rendezvous(request,pk):
    rdv=get_object_or_404(RendezVous,pk=pk); form=RendezVousForm(request.POST or None,instance=rdv)
    if form.is_valid(): form.save(); messages.success(request,'Rendez-vous modifié.'); return redirect('liste_rendezvous')
    return render(request,'RendezVous/formulaire.html',{'form':form,'titre':'Modifier le rendez-vous'})
@login_required
def supprimer_rendezvous(request,pk):
    rdv=get_object_or_404(RendezVous,pk=pk)
    if request.method=='POST': rdv.delete(); messages.success(request,'Rendez-vous supprimé.'); return redirect('liste_rendezvous')
    return render(request,'Cabinet/confirmer_suppression.html',{'objet':rdv,'retour':'liste_rendezvous'})
