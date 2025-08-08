class vehicale:
    def __init__(self, name, fareperson):
            self.name = name
            self.fareperson = fareperson

    def fare(self,passengers):
           return passengers * self.fareperson
class bus(vehicale):
      def fare(self,passengers):
            total_fare = super().fare(passengers)
            total_fare += total_fare *0.10
            return total_fare  
bus =bus("school volvo",50 )
passengers = 30
print("Total fare for bus is:",bus.fare(passengers))