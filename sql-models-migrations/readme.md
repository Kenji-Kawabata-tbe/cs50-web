20250225 40:01

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
