class Point():
    def __init__(self, input1, input2): 
        self.x = input1
        self.y = input2


p = Point(2, 8)


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
people = ["Henrique", "Theo", "Nei", "Niara"]
for person in people:
    

    if flight.add_passenger(person):
        print(f"Booked successfully!!!! {person}")
    else:
        print(f"Too Late, {person}!!!")