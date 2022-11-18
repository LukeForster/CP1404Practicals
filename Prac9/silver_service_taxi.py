from Prac9.taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = self.fanciness * self.price_per_km



