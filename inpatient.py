from patient import Patient


class InPatient(Patient):
    def __init__(self, name, age, phone, patient_id, medical_history, has_insurance, days, daily_rate):
        super().__init__(name, age, phone, patient_id, medical_history, has_insurance)

        self._days = days
        self._daily_rate = daily_rate

    def calculate_bill(self):
        total = self._days * self._daily_rate

        # Feature - insurance discount, 20% discount

        if self._has_insurance:
            total = total * 0.8   

        return total