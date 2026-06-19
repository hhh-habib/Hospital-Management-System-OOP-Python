from datetime import datetime


class Prescription:
    def __init__(self, medicine_name, dosage, duration, prescribed_by, prescribed_date=None):
        self._medicine_name = medicine_name
        self._dosage = dosage
        self._duration = duration
        self._prescribed_by = prescribed_by
        self._prescribed_date = prescribed_date if prescribed_date else datetime.now().strftime("%Y-%m-%d")

    @property
    def medicine_name(self):
        return self._medicine_name

    @property
    def dosage(self):
        return self._dosage

    @property
    def duration(self):
        return self._duration

    @property
    def prescribed_by(self):
        return self._prescribed_by

    @property
    def prescribed_date(self):
        return self._prescribed_date

    def get_details(self):
        return (f"Medicine: {self._medicine_name}, "
                f"Dosage: {self._dosage}, "
                f"Duration: {self._duration} days, "
                f"Prescribed by: {self._prescribed_by._name}, "
                f"Date: {self._prescribed_date}")

    def to_dict(self, patient):
        return {
            'medicine_name': self._medicine_name,
            'dosage': self._dosage,
            'duration': self._duration,
            'prescribed_by_id': self._prescribed_by._doctor_id,
            'patient_id': patient._patient_id,
            'prescribed_date': self._prescribed_date
        }

    @classmethod
    def from_dict(cls, data, patient, prescribed_by):
        return cls(
            data['medicine_name'],
            data['dosage'],
            data['duration'],
            prescribed_by,
            data.get('prescribed_date')
        )

    def __str__(self):
        return self.get_details()

    def __repr__(self):
        return f"Prescription({self._medicine_name}, {self._dosage}, {self._duration})"
