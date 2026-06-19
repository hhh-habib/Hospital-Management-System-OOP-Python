from doctor import Doctor


class SpecialistDoctor(Doctor):
    def __init__(self, name, age, phone, doctor_id, specialty, fee, specialization, consultation_fee):
        super().__init__(name, age, phone, doctor_id, specialty, fee)
        self._specialization = specialization
        self._consultation_fee = consultation_fee

    @property
    def specialization(self):
        return self._specialization

    @property
    def consultation_fee(self):
        return self._consultation_fee

    def display_info(self):
        return (f"Specialist Doctor ID: {self._doctor_id}, "
                f"Name: {self._name}, "
                f"Specialty: {self._specialty}, "
                f"Base Fee: {self._fee}, "
                f"Specialization: {self._specialization}, "
                f"Consultation Fee: {self._consultation_fee}")

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return f"SpecialistDoctor({self._doctor_id}, {self._name}, {self._specialization})"
