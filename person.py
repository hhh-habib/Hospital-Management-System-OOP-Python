
class Person:

    def __init__(self, name, age, phone):
        self._name = name
        self._age = age
        self._phone = phone

    def display_info(self):
        return f"Name: {self._name}, Age: {self._age}, Phone: {self._phone}"
