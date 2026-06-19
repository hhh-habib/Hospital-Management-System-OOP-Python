from person import Person


class Doctor(Person):
    def __init__(self, name, age, phone, doctor_id, specialty, fee):
        super().__init__(name, age, phone)

        self._doctor_id = doctor_id
        self._specialty = specialty
        self._fee = fee

    def display_info(self):
        return f"Doctor ID: {self._doctor_id}, Name: {self._name}, Specialty: {self._specialty}, Fee: {self._fee}"

    def to_dict(self):
        return {
            'doctor_type': 'Doctor',
            'doctor_id': self._doctor_id,
            'name': self._name,
            'age': self._age,
            'phone': self._phone,
            'specialty': self._specialty,
            'fee': self._fee
        }