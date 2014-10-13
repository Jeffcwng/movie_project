from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from movie_app.models import *
from django.forms import ModelForm


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Watcher
        fields = ("username", "first_name", "last_name", "phone", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Watcher.objects.get(username=username)
        except Watcher.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class TheaterForm(ModelForm):
    class Meta:
        model = Theater

class MovieForm(ModelForm):
    class Meta:
        model = Movie

class ShowtimeForm(ModelForm):
    class Meta:
        model = Showtime

class SeatForm(ModelForm):
    class Meta:
        model = Seat


class TicketForm(ModelForm):
    class Meta:
        model = Ticket


