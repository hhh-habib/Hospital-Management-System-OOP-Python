from abc import ABC, abstractmethod
from person import Person


class Patient(Person, ABC):
    def __init__(self, name, age, phone, patient_id, medical_history, has_insurance):
        super().__init__(name, age, phone)

        self._patient_id = patient_id
        self._medical_history = medical_history
        self._has_insurance = has_insurance
        self._appointments = []
        self._prescriptions = []

    @abstractmethod
    def calculate_bill(self):
       pass

    def add_appointment(self, appointment):
       self._appointments.append(appointment)

    def view_history(self):
       return self._appointments
     
    def add_prescription(self, prescription):
       self._prescriptions.append(prescription)

    def view_prescriptions(self):
       return self._prescriptions

    def to_dict(self):
       return {
           'patient_type': self.__class__.__name__,
           'name': self._name,
           'age': self._age,
           'phone': self._phone,
           'patient_id': self._patient_id,
           'medical_history': self._medical_history,
           'has_insurance': self._has_insurance
       }
     
    def __gt__(self, other):
       return self.calculate_bill() > other.calculate_bill()


def get_patient_input():
    """Collect common patient info"""
    return {
       'name': input("Name: "),
       'age': int(input("Age: ")),
       'phone': input("Phone: "),
       'pid': input("Patient ID: ")
    }


def show_menu():
    options = [
       "Add InPatient", "Add OutPatient", "Add Doctor",
       "Book Appointment", "Show Bills", "Exit"
    ]
    for i, opt in enumerate(options, 1):
       print(f"{i}. {opt}")