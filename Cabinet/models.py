from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


def valider_date_naissance(value):
    if value >= date.today():
        raise ValidationError("La date de naissance doit être antérieure à aujourd'hui.")


telephone_validator = RegexValidator(r'^\d{8}$', "Le téléphone doit contenir exactement 8 chiffres.")
cin_validator = RegexValidator(r'^\d{8}$', "Le CIN doit contenir exactement 8 chiffres.")


class User(AbstractUser):
    """Utilisateur Django personnalisé (username, password, email, first_name, last_name hérités)."""

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


class Specialite(models.Model):
    nom_specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_specialite


class Medecin(User):
    matricule_ordre = models.CharField(
        max_length=6, primary_key=True, validators=[MinLengthValidator(6)]
    )
    telephone = models.CharField(max_length=8, validators=[telephone_validator])
    specialites = models.ManyToManyField(Specialite, related_name='medecins')

    class Meta:
        verbose_name = "Médecin"
        verbose_name_plural = "Médecins"

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"


class Patient(User):
    cin = models.CharField(max_length=8, primary_key=True, validators=[cin_validator])
    telephone = models.CharField(max_length=8, validators=[telephone_validator])
    date_naissance = models.DateField(validators=[valider_date_naissance])

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"