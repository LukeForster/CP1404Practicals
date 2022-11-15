"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


# class PointerArithmetic:
#     """"""
#
#     def __init__(self, is_arithmetic):
#         self.is_arithmetic = is_arithmetic
#
#     def is_arithmetic(self):
#         return self.is_arithmetic() is True


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year,pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.PointerArithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}," \
               f" Pointer Arithmetic = {self.PointerArithmetic}"
    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, True)

    languages = [ruby, python, visual_basic]
    print(languages)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
        # for details in language:
        #     if language[1] == 'Dynamic Typing':
        #         print(language[0])
        #     if language[4] is True:
        #         print(language[0])


if __name__ == "__main__":
    run_tests()
