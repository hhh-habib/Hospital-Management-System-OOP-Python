import unittest
from inpatient import InPatient
from outpatient import OutPatient
from doctor import Doctor
from prescription import Prescription


class PatientTests(unittest.TestCase):
    def test_inpatient_bill(self):
        patient = InPatient('Alice', 40, '555-1010', 'P100', 'History', True, 5, 200)
        self.assertAlmostEqual(patient.calculate_bill(), 800.0)

    def test_outpatient_bill(self):
        patient = OutPatient('Bob', 35, '555-2020', 'P101', 'History', False, 3, 100)
        self.assertEqual(patient.calculate_bill(), 300)

    def test_prescription_tracking(self):
        patient = InPatient('Alice', 40, '555-1010', 'P100', 'History', False, 1, 100)
        doctor = Doctor('Dr. House', 50, '555-3030', 'D100', 'Diagnostics', 250)
        prescription = Prescription('Ibuprofen', '200mg', 5, doctor)
        patient.add_prescription(prescription)
        self.assertEqual(len(patient.view_prescriptions()), 1)
        self.assertEqual(patient.view_prescriptions()[0].medicine_name, 'Ibuprofen')


if __name__ == '__main__':
    unittest.main()
