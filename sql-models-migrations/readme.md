20250225 40:01
20250226 1:10:45
20250227 Lesson Done 1:54:07


sqlite3 flights.sql

CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

.tables

SELECT * FROM flights;

INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);

SELECT * FROM flights;

INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);

.mode columns * SELECTでヘッダーが表示される
.headers yes  * SELECTでヘッダーが表示される

SELECT * FROM flights;
SELECT * FROM flights WHERE origin = "New York";
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
SELECT * FROM flights WHERE origin in ("New York", "Lima");
SELECT * FROM flights WHERE origin LIKE "%a%";

UPDATE flights
    SET duration = 430
    WHERE origin = "New York";

DELETE FROM flights WHERE destination = "Tokyo";

SELECT first, origin, destination
FROM flights JOIN passengers
ON passengers.flight_id = flights.id;


django-admin startproject airline
python manage.py startapp flights
airline/settings.pyのINSTALLED_APPSにflightsを追加する
airline/urls.pyのfrom django.urls import pathに includeのimportを追加、urlpatternsにpath('flights/', include("flights.urls")),を追加する
flights/urls.pyを作成し、必要に応じてviews.pyを編集
flights/models.py
# models.pyに施された変更を探して、マイグレーションファイルを作成
python manage.py makemigrations
# 反映
python manage.py migrate
python manage.py shell
>>> from flights.models import Flight
>>> f = Flight(origin="New York", destination="London", duration=415)
>>> f.save()
>>> Flight.objects.all()

>>> from flights.models import Flight
>>> flights = Flight.objects.all()
>>> flights

>>> flight = flights.first()
>>> flight
>>> flight.id
>>> flight.origin
>>> flight.destination
>>> flight.duration
>>> flight.delete()

# Import all models
>>> from flights.models import *

# Create some new airports
>>> jfk = Airport(code="JFK", city="New York")
>>> lhr = Airport(code="LHR", city="London")
>>> cdg = Airport(code="CDG", city="Paris")
>>> nrt = Airport(code="NRT", city="Tokyo")
>>> Airport.objects.all()
>>> Airport.objects.filter(city="New York")
>>> Airport.objects.get(city="New York")

# Save the airports to the database
>>> jfk.save()
>>> lhr.save()
>>> cdg.save()
>>> nrt.save()

# Add a flight and save it to the database
>>> f = Flight(origin=jfk, destination=lhr, duration=414)
>>> f.save()
>>> f
    <Flight: 1: New York (JFK) to London (LHR)>
>>> f.origin
    <Airport: New York (JFK)>
>>> jfk.departures.all() # jfkがoriginに設定されているFlight
    <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>
>>> lhr.arrivals.all() # lhrがdestinationに設定されているFlight
    <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>

>>> jfk = Airport.objects.get(city="New York")
>>> cdg = Airport.objects.get(city="Paris")
>>> cdg
>>> f = Flight(origin=jfk, destination=cdg, duration=435)
>>> f.save()

passengers
