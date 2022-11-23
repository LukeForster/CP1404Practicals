

class Band:

    def __init__(self, name=""):
        """Construct a Musician with a name and empty instrument collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of the Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.musicians:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.musicians[0]}"
