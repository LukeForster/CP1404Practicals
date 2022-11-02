""" ETA: 20mins
    Start Time: 5:19pm"""


class ProgrammingLanguage:
    """Programming language Class"""

    def __init__(self, typing, name, year, reflection):
        self.typing = typing
        self.name = name
        self.year = year
        self.reflection = reflection

    def is_dynamic(self):
        # is_dynamic = input('is the typing Dynamic (T/F').upper()
        # try:
        #     if is_dynamic == 'T'
        #         return self.typing == 'Dynamic'
        #     else:
        #         return self.typing == 'Static'
        # except ValueError:
        #     print('Invalid input, True will be used')
        return is_dynamic == 'Dynamic'

    def __str__(self):
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year})



