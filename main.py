from hospital import Hospital
from inpatient import InPatient
from outpatient import OutPatient
from doctor import Doctor
from specialist_doctor import SpecialistDoctor

h = Hospital()

while True:
    print("1. Add InPatient")
    print("2. Add OutPatient")
    print("3. Add Doctor")
    print("4. Book Appointment")
    print("5. Show Bills")
    print("6. Exit")

    choice = input("Enter choice: ")



    if choice == "1":

        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        pid = input("Patient ID: ")
        days = int(input("Days: "))
        rate = float(input("Daily Rate: "))
        ins = input("Insurance (yes/no): ") == "yes"

        p = InPatient(name, age, phone, pid, "None", ins, days, rate)
        h.add_patient(p)

        print(f"InPatient added successfully")




    elif choice == "2":

        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        pid = input("Patient ID: ")
        visits = int(input("Visits: "))
        fee = float(input("Visit Fee: "))
        ins = input("Insurance (yes/no): ") == "yes"

        p = OutPatient(name, age, phone, pid, "None", ins, visits, fee)
        h.add_patient(p)

        print("OutPatient added successfully")




    elif choice == "3":

       print("1. Add Regular Doctor")
       print("2. Add Specialist Doctor")
       doc_choice = input("Enter choice: ")

       name = input("Name: ")
       age = int(input("Age: "))
       phone = input("Phone: ")
       did = input("Doctor ID: ")
       spec = input("Specialty: ")
       fee = float(input("Fee: "))

       if doc_choice == "2":
           specialization = input("Specialization: ")
           consultation_fee = float(input("Consultation Fee: "))
           d = SpecialistDoctor(name, age, phone, did, spec, fee, specialization, consultation_fee)
       else:
           d = Doctor(name, age, phone, did, spec, fee)

       h.add_doctor(d)

       print("Doctor added successfully")




    elif choice == "4":

        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")

        try:
            msg = h.book_appointment(pid, did)
            print(msg)
        except Exception as e:
            print(e)





    elif choice == "5":

        for p in h._patients:
            print(f"Patient ID: {p._patient_id}, Bill: {p.calculate_bill()}")
    




    elif choice == "6":
        break
    

    
    





