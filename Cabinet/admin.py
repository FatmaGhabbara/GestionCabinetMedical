from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Specialite, Medecin, Patient


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_specialite')
    search_fields = ('nom_specialite',)


@admin.register(Medecin)
class MedecinAdmin(UserAdmin):
    list_display = ('matricule_ordre', 'username', 'first_name', 'last_name', 'telephone')
    filter_horizontal = ('specialites',)
    fieldsets = UserAdmin.fieldsets + (
        ('Informations médecin', {'fields': ('matricule_ordre', 'telephone', 'specialites')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations médecin', {'fields': ('matricule_ordre', 'telephone', 'specialites')}),
    )


@admin.register(Patient)
class PatientAdmin(UserAdmin):
    list_display = ('cin', 'username', 'first_name', 'last_name', 'telephone')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations patient', {'fields': ('cin', 'telephone', 'date_naissance')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations patient', {'fields': ('cin', 'telephone', 'date_naissance')}),
    )