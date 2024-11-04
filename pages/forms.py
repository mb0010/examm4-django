from django import forms
from .models import Film, Ticket, Theatr, User, Orders

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'janr', 'date', 'image', 'film', 'treiler']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['place', 'vip']

class TheatrForm(forms.ModelForm):
    class Meta:
        model = Theatr
        fields = ['name', 'location']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone_number', 'email', 'username']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['user', 'online_shop', 'total_amount', 'status']
