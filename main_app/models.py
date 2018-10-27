from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Departement(models.Model):
    codeDept = models.CharField(primary_key=True, max_length=10)
    libelleDept = models.CharField(max_length=50)

    def __str__(self):
        return self.codeDept


class Enseignant(models.Model):
    codeEnseignant = models.OneToOneField(User, on_delete=models.CASCADE)
    nomEnseignant = models.CharField(max_length=25)
    prenomEnseignant = models.CharField(max_length=25)
    codeDept = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomEnseignant + ' - ' + self.prenomEnseignant


class Filiere(models.Model):
    CodeFiliere = models.CharField(primary_key=True, max_length=10)
    libelleFiliere = models.CharField(max_length=200)
    codeDept = models.ForeignKey(Departement, on_delete=models.CASCADE)
    PeriodeAccreditation = models.CharField(blank=True, max_length=9)

    def __str__(self):
        return self.CodeFiliere + ' - ' + self.libelleFiliere


class Salle(models.Model):
    SALLE_CHOICES = (
        ('td', 'TD'),
        ('tp', 'TP'),
        ('cm', 'CM'),
    )
    Id_Salle = models.CharField(primary_key=True, max_length=10)
    TypeSalle = models.CharField(max_length=15, choices=SALLE_CHOICES)
    Capacite = models.IntegerField(blank=False, default=1)
    Batiment = models.CharField(max_length=25)

    def __str__(self):
        return self.Id_Salle


class Horaire(models.Model):
    NumCreneauHoraire = models.IntegerField(primary_key=True)
    Duree = models.FloatField(blank=False, null=False, default=1.5)
    HeureDebut = models.TimeField(default=timezone.now)
    HeureFin = models.TimeField(default=timezone.now)

    class Meta:
        ordering = ('NumCreneauHoraire',)

    def __str__(self):
        return str(self.NumCreneauHoraire)


class Classe(models.Model):
    Id_Classe = models.CharField(primary_key=True, max_length=15)
    LibelleClasse = models.CharField(blank=True, max_length=35)
    Effectif = models.IntegerField(blank=False, null=False, default=1)
    CodeFiliere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return self.Id_Classe


class Module(models.Model):
    CodeModule = models.CharField(primary_key=True, max_length=20)
    LibelleModule = models.CharField(max_length=200)
    semestre = models.CharField(max_length=2)
    CodeFiliere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return self.CodeModule


class Matiere(models.Model):
    codeMatiere = models.CharField(primary_key=True, max_length=20)
    LibelleMatiere = models.CharField(max_length=150)
    CodeModule = models.ForeignKey(Module, on_delete=models.CASCADE)
    Coefficient = models.FloatField(blank=False, null=False, default=0)
    VH_Cours = models.IntegerField(blank=False, null=False, default=0)
    VH_TD = models.IntegerField(blank=False, null=False, default=0)
    VH_TP = models.IntegerField(blank=False, null=False, default=0)
    VH_EC = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.LibelleMatiere


class Cours(models.Model):
    JOURS_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeud', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
    )
    COURS_CHOICES = (
        ('td', 'TD'),
        ('tp', 'TP'),
        ('cm', 'CM'),
    )
    CodeEnseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    Id_Classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    Id_Salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    Id_Creneau = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    NumSemaine = models.IntegerField(blank=False, null=False, default=1)
    Jour = models.CharField(max_length=15, choices=JOURS_CHOICES)
    CodeMatiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    TypeCours = models.CharField(max_length=15, choices=COURS_CHOICES)

    def __str__(self):
        return str(self.NumSemaine)

class Reservation(models.Model):
    JOURS_CHOICES = (
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeud', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
    )
    codeReservation = models.AutoField(primary_key=True)
    codeEnseignant = models.ForeignKey(User, on_delete=models.CASCADE)
    NumCreneauHoraire = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    Id_Salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    NumSemaine = models.IntegerField(blank=False, null=False, default=1)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    jourReservation = models.CharField(max_length=15, choices=JOURS_CHOICES, default='Lundi')


    def __str__(self):
        return str(self.codeReservation) + ' - ' + str(Enseignant.nomEnseignant) + ' - ' + str(self.NumSemaine)





