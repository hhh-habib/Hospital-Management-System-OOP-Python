import unittest
from prescription import Prescription
from doctor import Doctor
from inpatient import InPatient


class PrescriptionTests(unittest.TestCase):
    def test_prescription_data(self):
        doctor = Doctor('Dr. Jay', 50, '555-5050', 'D102', 'Internal', 180)
        prescription = Prescription('Amoxicillin', '500mg', 7, doctor, '2026-06-20')
        self.assertEqual(prescription.medicine_name, 'Amoxicillin')
        self.assertEqual(prescription.dosage, '500mg')
        self.assertEqual(prescription.duration, 7)
        self.assertEqual(prescription.prescribed_by._doctor_id, 'D102')
        self.assertEqual(prescription.prescribed_date, '2026-06-20')

    def test_prescription_serialization(self):
        patient = InPatient('Alice', 40, '555-1010', 'P100', 'History', False, 1, 100)
        doctor = Doctor('Dr. Jay', 50, '555-5050', 'D102', 'Internal', 180)
        prescription = Prescription('Amoxicillin', '500mg', 7, doctor, '2026-06-20')
        data = prescription.to_dict(patient)
        self.assertEqual(data['patient_id'], 'P100')
        self.assertEqual(data['prescribed_by_id'], 'D102')
        loaded = Prescription.from_dict(data, patient, doctor)
        self.assertEqual(loaded.medicine_name, 'Amoxicillin')


if __name__ == '__main__':
    unittest.main()
