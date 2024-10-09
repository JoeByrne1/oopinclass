import random

class Insect: #MIDTERM (10/7)
    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.name = n
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight
    
    def get_name(self):
        return self.name