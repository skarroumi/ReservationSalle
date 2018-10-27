
from django.contrib import admin

# Register your models here.
from . models import Enseignant, Filiere, Salle, Departement, Classe, Horaire, Module, Matiere, Cours, Reservation


class DepartementAdmin(admin.ModelAdmin):

    list_display = ('codeDept', 'libelleDept')


admin.site.register(Departement, DepartementAdmin)


class FiliereAdmin(admin.ModelAdmin):
    list_display = ('CodeFiliere', 'libelleFiliere', 'codeDept', 'PeriodeAccreditation')


admin.site.register(Filiere, FiliereAdmin)


class SalleAdmin(admin.ModelAdmin):
    list_display = ('Id_Salle', 'TypeSalle', 'Capacite', 'Batiment')


admin.site.register(Salle, SalleAdmin)


class HoraireAdmin(admin.ModelAdmin):
    list_display = ('NumCreneauHoraire', 'Duree', 'HeureDebut', 'HeureFin')


admin.site.register(Horaire, HoraireAdmin)


class ClasseAdmin(admin.ModelAdmin):
    list_display = ('Id_Classe', 'LibelleClasse', 'Effectif', 'CodeFiliere')


admin.site.register(Classe, ClasseAdmin)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('CodeModule', 'LibelleModule', 'semestre', 'CodeFiliere')


admin.site.register(Module, ModuleAdmin)


class MatiereAdmin(admin.ModelAdmin):
    list_display = ('codeMatiere', 'LibelleMatiere', 'CodeModule', 'Coefficient', 'VH_Cours', 'VH_TD', 'VH_TP', 'VH_EC')


admin.site.register(Matiere, MatiereAdmin)


class CoursAdmin(admin.ModelAdmin):
    list_display = ('CodeEnseignant', 'Id_Classe', 'Id_Salle', 'Id_Creneau', 'NumSemaine', 'Jour', 'CodeMatiere', 'TypeCours')


admin.site.register(Cours, CoursAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('NumCreneauHoraire', 'codeEnseignant', 'Id_Salle', 'NumSemaine', 'jourReservation',  'date_creation')


admin.site.register(Reservation,ReservationAdmin)


class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('codeEnseignant', 'nomEnseignant', 'prenomEnseignant', 'codeDept')


admin.site.register(Enseignant, EnseignantAdmin)

