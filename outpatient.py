from patient import Patient


class OutPatient(Patient):
    def __init__(self, name, age, phone, patient_id, medical_history, has_insurance, visits, visit_fee):
        super().__init__(name, age, phone, patient_id, medical_history, has_insurance)

        self._visits = visits
        self._visit_fee = visit_fee

    def calculate_bill(self):
        total = self._visits * self._visit_fee

        # Feature - insurance discout (20%)

        if self._has_insurance:
            total = total * 0.8

        return total

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'visits': self._visits,
            'visit_fee': self._visit_fee
        })
        return data