import atexit
import json
import os
from datetime import datetime

from appointment import Appointment
from exceptions import PatientNotFoundError
from inpatient import InPatient
from outpatient import OutPatient
from doctor import Doctor
from specialist_doctor import SpecialistDoctor
from prescription import Prescription


class Hospital:
    PATIENTS_FILE = "patients.json"
    DOCTORS_FILE = "doctors.json"
    APPOINTMENTS_FILE = "appointments.json"
    PRESCRIPTIONS_FILE = "prescriptions.json"

    def __init__(self):
        self._patients = []
        self._doctors = []
        self._appointments = []

        self._load_data()
        atexit.register(self.save_all)

    def add_patient(self, patient):
        self._patients.append(patient)

    def add_doctor(self, doctor):
        self._doctors.append(doctor)

    def _get_file_path(self, filename):
        return os.path.join(os.path.dirname(__file__), filename)

    def _read_json(self, filename):
        filepath = self._get_file_path(filename)
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write_json(self, filename, data):
        filepath = self._get_file_path(filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _create_patient_from_dict(self, data):
        patient_type = data.get("patient_type", "OutPatient")
        if patient_type == "InPatient":
            return InPatient(
                data["name"],
                data["age"],
                data["phone"],
                data["patient_id"],
                data["medical_history"],
                data["has_insurance"],
                data.get("days", 0),
                data.get("daily_rate", 0.0),
            )
        return OutPatient(
            data["name"],
            data["age"],
            data["phone"],
            data["patient_id"],
            data["medical_history"],
            data["has_insurance"],
            data.get("visits", 0),
            data.get("visit_fee", 0.0),
        )

    def _create_doctor_from_dict(self, data):
        doctor_type = data.get("doctor_type", "Doctor")
        if doctor_type == "SpecialistDoctor":
            return SpecialistDoctor(
                data["name"],
                data["age"],
                data["phone"],
                data["doctor_id"],
                data["specialty"],
                data["fee"],
                data.get("specialization", ""),
                data.get("consultation_fee", 0.0),
            )
        return Doctor(
            data["name"],
            data["age"],
            data["phone"],
            data["doctor_id"],
            data["specialty"],
            data["fee"],
        )

    def _load_data(self):
        self._load_patients()
        self._load_doctors()
        self._load_appointments()
        self._load_prescriptions()

    def _load_patients(self):
        self._patients = []
        for data in self._read_json(self.PATIENTS_FILE):
            self._patients.append(self._create_patient_from_dict(data))

    def _load_doctors(self):
        self._doctors = []
        for data in self._read_json(self.DOCTORS_FILE):
            self._doctors.append(self._create_doctor_from_dict(data))

    def _load_appointments(self):
        self._appointments = []
        for data in self._read_json(self.APPOINTMENTS_FILE):
            patient = self.find_patient(data["patient_id"])
            doctor = self.find_doctor(data["doctor_id"])
            appointment = Appointment.from_dict(data, patient, doctor)
            self._appointments.append(appointment)
            patient.add_appointment(appointment)

    def _load_prescriptions(self):
        for data in self._read_json(self.PRESCRIPTIONS_FILE):
            patient = self.find_patient(data["patient_id"])
            doctor = self.find_doctor(data["prescribed_by_id"])
            prescription = Prescription.from_dict(data, patient, doctor)
            patient.add_prescription(prescription)

    def save_all(self):
        self._write_json(self.PATIENTS_FILE, [p.to_dict() for p in self._patients])
        self._write_json(self.DOCTORS_FILE, [d.to_dict() for d in self._doctors])
        self._write_json(self.APPOINTMENTS_FILE, [a.to_dict() for a in self._appointments])
        prescriptions = []
        for patient in self._patients:
            for prescription in patient.view_prescriptions():
                prescriptions.append(prescription.to_dict(patient))
        self._write_json(self.PRESCRIPTIONS_FILE, prescriptions)

    def find_patient(self, patient_id):
        for p in self._patients:
            if p._patient_id == patient_id:

                return p
        raise PatientNotFoundError(f"Patient {patient_id} not found")
    


    def find_doctor(self, doctor_id):
        for d in self._doctors:
            if d._doctor_id == doctor_id:
                
                return d
        raise Exception(f"Doctor {doctor_id} not found")
    

    
    def book_appointment(self, patient_id, doctor_id):
        patient = self.find_patient(patient_id)
        doctor = self.find_doctor(doctor_id)

        appointment_id = max((a.appointment_id for a in self._appointments), default=0) + 1
        appointment = Appointment(appointment_id, patient, doctor, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self._appointments.append(appointment)

        # Feature - appointment history
        patient.add_appointment(appointment)

        return f"Appointment booked successfully"
    


