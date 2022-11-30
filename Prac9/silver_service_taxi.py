from Prac9.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = self.fanciness * self.price_per_km

    def get_fare_fee(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"
