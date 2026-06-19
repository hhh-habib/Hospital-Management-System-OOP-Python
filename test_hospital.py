import os
import unittest
from hospital import Hospital
from inpatient import InPatient
from doctor import Doctor


class HospitalPersistenceTests(unittest.TestCase):
    def setUp(self):
        self.original_patient_file = Hospital.PATIENTS_FILE
        self.original_doctor_file = Hospital.DOCTORS_FILE
        self.original_appointment_file = Hospital.APPOINTMENTS_FILE
        self.original_prescription_file = Hospital.PRESCRIPTIONS_FILE

        Hospital.PATIENTS_FILE = 'test_patients.json'
        Hospital.DOCTORS_FILE = 'test_doctors.json'
        Hospital.APPOINTMENTS_FILE = 'test_appointments.json'
        Hospital.PRESCRIPTIONS_FILE = 'test_prescriptions.json'

        self.files = [
            Hospital.PATIENTS_FILE,
            Hospital.DOCTORS_FILE,
            Hospital.APPOINTMENTS_FILE,
            Hospital.PRESCRIPTIONS_FILE,
        ]

        for filename in self.files:
            if os.path.exists(filename):
                os.remove(filename)

        self.hospital = Hospital()

    def tearDown(self):
        for filename in self.files:
            if os.path.exists(filename):
                os.remove(filename)

        Hospital.PATIENTS_FILE = self.original_patient_file
        Hospital.DOCTORS_FILE = self.original_doctor_file
        Hospital.APPOINTMENTS_FILE = self.original_appointment_file
        Hospital.PRESCRIPTIONS_FILE = self.original_prescription_file

    def test_appointment_booking_persistence(self):
        patient = InPatient('Test', 30, '555-6060', 'P200', 'None', False, 2, 100)
        doctor = Doctor('Dr. Gray', 55, '555-7070', 'D200', 'Orthopedics', 200)
        self.hospital.add_patient(patient)
        self.hospital.add_doctor(doctor)
        result = self.hospital.book_appointment('P200', 'D200')
        self.assertEqual(result, 'Appointment booked successfully')

        self.hospital.save_all()
        loaded = Hospital()
        self.assertEqual(len(loaded._patients), 1)
        self.assertEqual(len(loaded._doctors), 1)
        self.assertEqual(len(loaded._appointments), 1)
        self.assertEqual(loaded._appointments[0].patient._patient_id, 'P200')
        self.assertEqual(loaded._appointments[0].doctor._doctor_id, 'D200')
        self.assertNotEqual(loaded._appointments[0].appointment_date, '2025-01-15')


if __name__ == '__main__':
    unittest.main()
