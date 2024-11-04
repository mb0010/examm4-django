from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user-list')
    return render(request, 'user_confirm_delete.html', {'user': user})
def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films})

def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film-list')
    else:
        form = FilmForm()
    return render(request, 'film_form.html', {'form': form})

def film_update(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film-list')  # Redirect to your film list page
    else:
        form = FilmForm(instance=film)
    return render(request, 'film_form.html', {'form': form, 'film': film})

def film_delete(request, pk):
    film = Film.objects.get(pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('film-list')
    return render(request, 'film_confirm_delete.html', {'film': film})
from .models import Ticket
from .forms import TicketForm

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket-list')
    else:
        form = TicketForm()
    return render(request, 'ticket_form.html', {'form': form})

def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket-list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_form.html', {'form': form})

def ticket_delete(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket-list')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})
from .models import Orders
from .forms import OrdersForm

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrdersForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request, pk):
    order = Orders.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrdersForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, pk):
    order = Orders.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order-list')
    return render(request, 'order_confirm_delete.html', {'order': order})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
