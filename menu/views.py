from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Dish, Reservation, Contact
from .forms import ReservationForm
# Create your views here.

def home(request):
    return render(request, "menu/home.html")

def menu_page(request):
    dishes = Dish.objects.all()
    return render(request, "menu/menu.html", {"dishes": dishes})


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, "menu/reservation.html", {"form": form})




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_obj = Contact(
            name=name,
            email=email,
            message=message
        )
        contact_obj.save()

        return redirect('home')

    return render(request, "menu/contact.html")