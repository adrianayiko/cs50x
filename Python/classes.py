class Flight:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.free_seats():
            return False
        else:
            self.passengers.append(name)
            return True    
    def free_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Mark", "John","Esther"]
people.append("Aggrey")
print(people)
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")