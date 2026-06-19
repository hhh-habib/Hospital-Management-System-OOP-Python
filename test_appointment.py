import unittest
from appointment import Appointment
from doctor import Doctor
from inpatient import InPatient


class AppointmentTests(unittest.TestCase):
    def test_appointment_data(self):
        patient = InPatient('Alice', 40, '555-1010', 'P100', 'History', False, 1, 100)
        doctor = Doctor('Dr. Ray', 45, '555-4040', 'D101', 'Surgery', 300)
        appointment = Appointment(1, patient, doctor, '2026-06-20 10:00:00')
        self.assertEqual(appointment.appointment_id, 1)
        self.assertEqual(appointment.patient._patient_id, 'P100')
        self.assertEqual(appointment.doctor._doctor_id, 'D101')
        self.assertIn('Patient: Alice', appointment.get_details())

    def test_appointment_serialization(self):
        patient = InPatient('Alice', 40, '555-1010', 'P100', 'History', False, 1, 100)
        doctor = Doctor('Dr. Ray', 45, '555-4040', 'D101', 'Surgery', 300)
        appointment = Appointment(2, patient, doctor, '2026-06-20 10:00:00')
        data = appointment.to_dict()
        self.assertEqual(data['patient_id'], 'P100')
        self.assertEqual(data['doctor_id'], 'D101')
        self.assertEqual(data['appointment_date'], '2026-06-20 10:00:00')
        loaded = Appointment.from_dict(data, patient, doctor)
        self.assertEqual(loaded.appointment_id, 2)


if __name__ == '__main__':
    unittest.main()
