from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    #destination = models.CharField(max_length=64)
    # on_delete=models.CASCADE ここではAirportを削除した場合、それに対応するFlightも削除される
    # related_nameは逆参照を可能にする。AirportからFlightのoriginをdepartures、destinationをarrivalsとして参照できる。
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # この関数がオブジェクトの文字列表現を返す場合
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # flights属性を使ってそのPassengerに関連する全てのFlightにアクセスできる。
    # 同様にpassengersというrelated_nameを使ってそのFlightの全てのPassengerにアクセスできる。
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
