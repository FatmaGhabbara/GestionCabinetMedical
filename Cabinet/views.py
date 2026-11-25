from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MedecinForm, PatientForm, SpecialiteForm
from .models import Medecin, Patient, Specialite
@login_required
def accueil(request):
    from RendezVous.models import RendezVous
    return render(request,'Cabinet/accueil.html',{'nb_patients':Patient.objects.count(),'nb_medecins':Medecin.objects.count(),'nb_specialites':Specialite.objects.count(),'nb_rendezvous':RendezVous.objects.count(),'prochains':RendezVous.objects.select_related('patient','medecin').order_by('date_heure')[:5]})
@login_required
def liste_patients(request):
    q=request.GET.get('q',''); patients=Patient.objects.all()
    if q: patients=patients.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(cin__icontains=q))
    return render(request,'Cabinet/patients.html',{'patients':patients,'q':q})
@login_required
def ajouter_patient(request):
    form=PatientForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,'Patient ajouté.'); return redirect('liste_patients')
    return render(request,'Cabinet/formulaire.html',{'form':form,'titre':'Ajouter un patient'})
@login_required
def modifier_patient(request,cin):
    obj=get_object_or_404(Patient,cin=cin); form=PatientForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,'Patient modifié.'); return redirect('liste_patients')
    return render(request,'Cabinet/formulaire.html',{'form':form,'titre':'Modifier un patient'})
@login_required
def supprimer_patient(request,cin):
    obj=get_object_or_404(Patient,cin=cin)
    if request.method=='POST': obj.delete(); messages.success(request,'Patient supprimé.'); return redirect('liste_patients')
    return render(request,'Cabinet/confirmer_suppression.html',{'objet':obj,'retour':'liste_patients'})
@login_required
def liste_medecins(request):
    return render(request,'Cabinet/medecins.html',{'medecins':Medecin.objects.prefetch_related('specialites').all()})
@login_required
def ajouter_medecin(request):
    form=MedecinForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,'Médecin ajouté.'); return redirect('liste_medecins')
    return render(request,'Cabinet/formulaire.html',{'form':form,'titre':'Ajouter un médecin'})
@login_required
def modifier_medecin(request,matricule_ordre):
    obj=get_object_or_404(Medecin,matricule_ordre=matricule_ordre); form=MedecinForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,'Médecin modifié.'); return redirect('liste_medecins')
    return render(request,'Cabinet/formulaire.html',{'form':form,'titre':'Modifier un médecin'})
@login_required
def supprimer_medecin(request,matricule_ordre):
    obj=get_object_or_404(Medecin,matricule_ordre=matricule_ordre)
    if request.method=='POST': obj.delete(); messages.success(request,'Médecin supprimé.'); return redirect('liste_medecins')
    return render(request,'Cabinet/confirmer_suppression.html',{'objet':obj,'retour':'liste_medecins'})
@login_required
def liste_specialites(request):
    form=SpecialiteForm(request.POST or None)
    if request.method=='POST' and form.is_valid(): form.save(); messages.success(request,'Spécialité ajoutée.'); return redirect('liste_specialites')
    return render(request,'Cabinet/specialites.html',{'specialites':Specialite.objects.all(),'form':form})
@login_required
def supprimer_specialite(request,pk):
    obj=get_object_or_404(Specialite,pk=pk)
    if request.method=='POST': obj.delete(); messages.success(request,'Spécialité supprimée.')
    return redirect('liste_specialites')
