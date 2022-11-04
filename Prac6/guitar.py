import datetime

current_year = datetime.date.today().year


class Guitar:
    """Guitar Class"""
    def __init__(self, name='', year=0, cost=float(0)):
        """Defines self variables"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """'f' string returned for the new guitars"""
        return f'{self.name} ({self.year}) : {self.cost:,.2f}'

    def get_age(self):
        """Determines the age of the guitar"""
        print(f'In 2022 the {self.name} is: 2022-{self.year}= {2022 - int(self.year)}')
        return current_year - self.year

    def is_vintage(self):
        """Returns if the guitar is older than 50"""
        # is_vintage = False
        # if self.get_age() >= 50:
        #     is_vintage = True
        # return is_vintage
        return self.get_age() >= 50

    def __lt__(self, other):
        """Used so that the sort() function can be used in the guitars.py"""
        return self.year < other.year
