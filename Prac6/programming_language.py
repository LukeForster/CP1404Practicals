""" ETA: 20 mins
    Start Time: 5:19pm"""


class ProgrammingLanguage:
    """Programming language Class"""

    def __init__(self, name, typing, reflection, year):
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
        return self.typing == 'Dynamic'

    def __str__(self):
        return f'{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}'


def find_dynamic_languages():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    # print(python)
    print('The dynamically typed languages are:')
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == '__main__':
    find_dynamic_languages()
