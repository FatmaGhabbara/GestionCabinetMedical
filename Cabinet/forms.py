from django import forms
from .models import Medecin, Patient, Specialite
class MedecinForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,required=False,help_text='Obligatoire à la création.')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].required = self.instance.pk is None
    class Meta:
        model=Medecin
        fields=['username','password','first_name','last_name','email','matricule_ordre','telephone','specialites']
        widgets={'specialites':forms.CheckboxSelectMultiple()}
    def save(self,commit=True):
        obj=super().save(commit=False); pwd=self.cleaned_data.get('password')
        if pwd: obj.set_password(pwd)
        if commit: obj.save(); self.save_m2m()
        return obj
class PatientForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,required=False,help_text='Obligatoire à la création.')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].required = self.instance.pk is None
    class Meta:
        model=Patient
        fields=['username','password','first_name','last_name','email','cin','telephone','date_naissance']
        widgets={'date_naissance':forms.DateInput(attrs={'type':'date'})}
    def save(self,commit=True):
        obj=super().save(commit=False); pwd=self.cleaned_data.get('password')
        if pwd: obj.set_password(pwd)
        if commit: obj.save()
        return obj
class SpecialiteForm(forms.ModelForm):
    class Meta: model=Specialite; fields=['nom_specialite']
