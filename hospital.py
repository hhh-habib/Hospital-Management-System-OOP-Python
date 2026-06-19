from exceptions import PatientNotFoundError

class Hospital:
    def __init__(self):
        self._patients = []
        self._doctors = []
        self._appointments = []

    def add_patient(self, patient):
        self._patients.append(patient)

    def add_doctor(self, doctor):
        self._doctors.append(doctor)



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

        appointment = (patient, doctor)
        self._appointments.append(appointment)

        # Feature - appointment history

        patient.add_appointment(appointment)


        return f"Appointment booked successfully"
    


