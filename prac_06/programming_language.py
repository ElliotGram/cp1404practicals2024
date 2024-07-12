class ProgrammingLanguage:

    def __init__(self, name, typed, reflection, year):
        self.name = name
        self.typed = typed
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a book name type reflection and year"""
        return f"{self.name}, {self.typed}, {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if string is typed dynamically"""
        return self.typed == "Dynamic"
