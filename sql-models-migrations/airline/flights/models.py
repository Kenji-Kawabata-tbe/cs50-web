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
    # related_nameはdjangoが呼ぶときのエイリアスみたいな感じ？
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # この関数がオブジェクトの文字列表現を返す場合
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
