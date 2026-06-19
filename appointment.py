from datetime import datetime


class Appointment:
    def __init__(self, appointment_id, patient, doctor, appointment_date, appointment_status="pending"):
        self._appointment_id = appointment_id
        self._patient = patient
        self._doctor = doctor
        self._appointment_date = appointment_date
        self._appointment_status = appointment_status

    @property
    def appointment_id(self):
        return self._appointment_id

    @property
    def patient(self):
        return self._patient

    @property
    def doctor(self):
        return self._doctor

    @property
    def appointment_date(self):
        return self._appointment_date

    @property
    def appointment_status(self):
        return self._appointment_status

    @appointment_status.setter
    def appointment_status(self, status):
        self._appointment_status = status

    def get_details(self):
        return (f"Appointment ID: {self._appointment_id}, "
                f"Patient: {self._patient._name}, "
                f"Doctor: {self._doctor._name}, "
                f"Date: {self._appointment_date}, "
                f"Status: {self._appointment_status}")

    def to_dict(self):
        return {
            'appointment_id': self._appointment_id,
            'patient_id': self._patient._patient_id,
            'doctor_id': self._doctor._doctor_id,
            'appointment_date': self._appointment_date,
            'appointment_status': self._appointment_status
        }

    @classmethod
    def from_dict(cls, data, patient, doctor):
        return cls(
            data['appointment_id'],
            patient,
            doctor,
            data['appointment_date'],
            data.get('appointment_status', 'pending')
        )

    def __str__(self):
        return self.get_details()

    def __repr__(self):
        return f"Appointment({self._appointment_id}, {self._patient._patient_id}, {self._doctor._doctor_id})"
