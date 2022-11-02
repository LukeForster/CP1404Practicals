import datetime

current_year = datetime.date.today().year


class Guitar:

    def __init__(self, name='', year=0, cost=float(0)):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f'{self.name} ({self.year}) : {self.cost:,.2f}'

    def get_age(self):
        print(f'In 2022 the {self.name} is: 2022-{self.year}= {2022 - int(self.year)}')
        return current_year - self.year

    def is_vintage(self):
        # is_vintage = False
        # if self.get_age() >= 50:
        #     is_vintage = True
        # return is_vintage
        return self.get_age() >= 50

    def __lt__(self, other):
        """Used so that the sort() function can be used in the guitars.py"""
        return self.year < other.year
