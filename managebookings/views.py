from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import Managebookings
from booktable.models import Booktable
from library import CustomLib

managebookings_lib = CustomLib(Managebookings)
booktable_lib = CustomLib(Booktable)
user_lib = CustomLib(User)


# Create your views here.
def view_managebookings(request):
    booktable = Managebookings.objects.filter(booking_confirm=False)
    return render(request, 'managebookings/managebookings.html',{"booktable":booktable})

def update_managebookings(request, id):
    # booktable = Managebookings.objects.get(id=id)
    booktable = managebookings_lib.get_id_specific_data(id=id)
    booktable.booking_confirm = True 
    booktable.save()
    return redirect ('view_managebookings')

def delete_managebookings(request, id):
    # booktable = Managebookings.objects.get(id=id)
    booktable = managebookings_lib.get_id_specific_data(id=id)
    booktable.delete()
    return redirect ('view_managebookings')

def add_managebookings(request, id):
    # booktable = Managebookings.object.get(id=id)
    # user = User.objects.get(id=request.user.id)
    booktable = managebookings_lib.get_id_specific_data(id=id)
    user = user_lib.get_id_specific_data(id=request.user.id)
    booking_cost = Managebookings.price
    booktable = Managebookings(user=user, booktable=booktable, booking_cost=booking_cost, booking_confirm=False)
    booktable.save()
    return redirect('view_managebookings')

def view_history(request):
    booktable = Managebookings.objects.filter(booking_confirm=True)
    return render(request, 'managebookings/history.html',{"booktable":booktable})

    