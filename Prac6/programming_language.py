""" ETA: 20 minutes
    Start Time: 5:19pm
    Finish Time 6:30pm
    Total Time = 71 minutes"""


class ProgrammingLanguage:
    """Programming language Class"""

    def __init__(self, name, typing, reflection, year):
        """Defines self variables"""
        self.typing = typing
        self.name = name
        self.year = year
        self.reflection = reflection

    def is_dynamic(self):
        """Returns 'Dynamic' used for checking later"""
        return self.typing == 'Dynamic'

    def __str__(self):
        """'f' string returned for the programming languages"""
        return f'{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}'


def find_dynamic_languages():
    """Checks whether the language is dynamic"""
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
