''' Time ETA: 30mins
    Start Time: 11:04pm
    Actual Time: '''
from datetime import datetime
class Project:
    """Project Class"""

    def __init__(self, name='', start_date='', priority=int(0), cost=float(0), completion=int(0)):
        """Defines self variables"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion
        self.date = datetime.strptime(start_date, "%d/%m/%Y").date()

    def __str__(self):
        """'f' string returned for the new guitars"""
        return f'{self.name} ({self.start_date}) : {self.cost:,.2f} {self.priority}, {self.completion}'
    #
    # def get_age(self):
    #     """Determines the age of the guitar"""
    #     print(f'In 2022 the {self.name} is: 2022-{self.year}= {2022 - int(self.year)}')
    #     return current_year - self.year
    #
    # def is_vintage(self):
    #     """Returns if the guitar is older than 50"""
    #     # is_vintage = False
    #     # if self.get_age() >= 50:
    #     #     is_vintage = True
    #     # return is_vintage
    #     return self.get_age() >= 50
    #
    def __lt__(self, other):
        """Used so that the sort() function can be used"""
        return self.date < other.date
