from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # flight_idを主キーとするFlightを取得
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
         # Passengerクラスのrelated_nameでpassengersを指定しているのでPassengerクラスのflightsを逆参照をしている
        "passengers": flight.passengers.all(),
        # このFlightに乗るPassengerを除外
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        # flight_idを主キーとするFlightを取得
        flight = Flight.objects.get(pk=flight_id)
        # Passengerについての情報の取得
        #   主キーがpassengerという名前の入力フォームから渡されるintのPassenger
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # ↑のpassengerのflightsに最初に取得したFlightを追加する
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
