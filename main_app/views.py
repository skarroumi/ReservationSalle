from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Reservation, Cours
from.forms import ReservationForm, AfficherEtat
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Enseignant
from django.contrib.auth.models import User

User = get_user_model()


def index(request):
    if not request.user.is_authenticated:

        titre = "Connexion"
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.is_superuser:
                return redirect('/admin')
            else:
                print
                return redirect("/dashboard")

        return render(request, 'index.html', {"form": form, "titre": titre})

    else:
        return redirect('/dashboard')


def register_view(request):
    titre = "Inscription"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("/dashboard")
    context = {
        "form": form,
        "titre": titre
    }

    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def profil(request):
    if request.user.is_authenticated:
        enseignant_data = {'user': request.user}
        return render(request, 'profil.html', enseignant_data)
    else:
        return redirect('/')


def home_prof(request):
    if request.user.is_authenticated:
        form = AfficherEtat(request.POST or None)
        if form.is_valid():
            var = form.save(commit=False)
            var1 = Cours.objects.filter(NumSemaine=var.NumSemaine, Jour=var.Jour, Id_Creneau=var.Id_Creneau)

            return render(request, 'etat_template.html', {'var1': var1})
        return render(request, 'home_prof.html', {'form': form, 'user': request.user})
    else:
        return redirect('/')



def history(request):
    if request.user.is_authenticated:
        reservation_history = Reservation.objects.filter(codeEnseignant=request.user)
        return render(request, 'historique.html', {'reservation_history': reservation_history})
    else:
        return redirect('/')


def reservation(request):
    if request.user.is_authenticated:
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            commitFalse = form.save(commit=False)
            commitFalse.codeEnseignant=request.user
            detecterReservation = Reservation.objects.all()
            detecterCours = Cours.objects.all()

            for i in detecterCours:
                if commitFalse.NumCreneauHoraire == i.Id_Creneau and commitFalse.NumSemaine == i.NumSemaine and commitFalse.jourReservation==i.Jour:

                    return render(request, 'reservation.html', {'form': form, 'erreur': 'Erreur ', 'jourReserve': commitFalse.jourReservation, 'semaineReserve': commitFalse.NumSemaine, 'crenReserve': commitFalse.NumCreneauHoraire})

            for res in detecterReservation:
                if commitFalse.NumCreneauHoraire == res.NumCreneauHoraire and commitFalse.NumSemaine==res.NumSemaine and commitFalse.jourReservation==res.jourReservation:
                    return render(request, 'reservation.html', {'form': form, 'erreur_reservation': 'Erreur ', 'jourReserve': commitFalse.jourReservation, 'semaineReserve': commitFalse.NumSemaine, 'crenReserve': commitFalse.NumCreneauHoraire})

            form.save()
            return redirect('/history')
        return render(request, 'reservation.html', {'form': form})
    else:
        return redirect('/')


def supprimer_reservation(request, codeRes):
    reservation_id = Reservation.objects.get(codeReservation=codeRes)
    reservation_id.delete()
    return redirect('/reservation')

def afficher_etat(request):
    render(request, 'etat_template.html')