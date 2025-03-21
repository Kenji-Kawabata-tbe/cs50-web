#オブジェクト指向
# 情報を格納してアクションを実行できるオブジェクトを中心としたプログラミングのパラダイム、
# またはプログラミングについての考え方です。

class Point():
    def __init__(self, input1, input2):  # 自動的に呼び出されるメソッド
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    #success = flight.add_passenger(person)
    #if success:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
