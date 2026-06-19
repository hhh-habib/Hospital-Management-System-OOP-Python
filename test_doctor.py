import unittest
from doctor import Doctor
from specialist_doctor import SpecialistDoctor


class DoctorTests(unittest.TestCase):
    def test_doctor_display_info(self):
        doctor = Doctor('Dr. Stone', 45, '555-1234', 'D001', 'General', 150)
        self.assertIn('Doctor ID: D001', doctor.display_info())
        self.assertIn('Specialty: General', doctor.display_info())

    def test_specialist_doctor_polymorphism(self):
        specialist = SpecialistDoctor('Dr. Amy', 50, '555-5678', 'D002', 'Neurology', 200, 'Stroke', 300)
        info = specialist.display_info()
        self.assertIn('Specialist Doctor ID: D002', info)
        self.assertIn('Consultation Fee: 300', info)

    def test_doctor_to_dict(self):
        doctor = Doctor('Dr. Stone', 45, '555-1234', 'D001', 'General', 150)
        data = doctor.to_dict()
        self.assertEqual(data['doctor_id'], 'D001')
        self.assertEqual(data['doctor_type'], 'Doctor')


if __name__ == '__main__':
    unittest.main()
