from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Enseignant, Reservation
from .models import Cours
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='IDENTIFIANT')
    password = forms.CharField(label='MOT DE PASSE', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Cet enseignant n'existe pas")

            if not user.check_password(password):
                raise forms.ValidationError("Mot de passe incorrect")

            if not user.is_active:
                raise forms.ValidationError("Cet Enseignant n'est pas actif")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='MOT DE PASSE', widget=forms.PasswordInput)
    email2 = forms.EmailField(label="confirmer Adresse")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Les adresses ne sont pas les memes")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            forms.ValidationError("Adresse existe deja")
        return email


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['NumCreneauHoraire', 'Id_Salle', 'NumSemaine', 'jourReservation']


class AfficherEtat(forms.ModelForm):

    class Meta:
        model = Cours
        fields = ['Jour', 'Id_Creneau', 'NumSemaine']


