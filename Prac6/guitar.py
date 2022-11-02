class Guitar:

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f'{self.name} ({self.year}) : {self.cost}'

    def get_age(self, age=0):
        print(f'In 2022 the {self.name} is: 2022-{self.year}= {2022 - int(self.year)}')
        return 2022 - self.year


    def is_vintage(self):
        is_vintage = False
        if self.get_age() >= 50:
            return is_vintage is True




