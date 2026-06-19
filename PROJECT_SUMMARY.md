# Project Summary

## Overview
This Hospital Patient Management System is implemented using object-oriented Python. It supports inpatient and outpatient records, doctor management, appointment booking, prescription tracking, and JSON-based persistence.

## Classes

- `Person`
  - Base class for people with `name`, `age`, and `phone`.
- `Patient` (abstract)
  - Inherits from `Person`.
  - Stores `patient_id`, `medical_history`, insurance status, appointments, and prescriptions.
  - Defines an abstract `calculate_bill()` method.
- `InPatient`
  - Inherits from `Patient`.
  - Adds `days` and `daily_rate`.
  - Implements `calculate_bill()` with insurance discount.
- `OutPatient`
  - Inherits from `Patient`.
  - Adds `visits` and `visit_fee`.
  - Implements `calculate_bill()` with insurance discount.
- `Doctor`
  - Inherits from `Person`.
  - Stores `doctor_id`, `specialty`, and `fee`.
- `SpecialistDoctor`
  - Inherits from `Doctor`.
  - Adds `specialization` and `consultation_fee`.
  - Overrides `display_info()` using polymorphism.
- `Appointment`
  - Stores `appointment_id`, `patient`, `doctor`, `appointment_date`, and `appointment_status`.
  - Supports serialization via `to_dict()`/`from_dict()`.
- `Prescription`
  - Stores `medicine_name`, `dosage`, `duration`, `prescribed_by`, and `prescribed_date`.
  - Supports serialization via `to_dict()`/`from_dict()`.
- `Hospital`
  - Manages collections of patients, doctors, appointments, and prescriptions.
  - Automatically loads data from JSON files on startup and saves on exit.

## Inheritance Hierarchy

```text
Person
├─ Patient (abstract)
│  ├─ InPatient
│  └─ OutPatient
└─ Doctor
   └─ SpecialistDoctor
```

## OOP Concepts Used

- Encapsulation: class fields are stored as protected attributes (e.g. `_name`, `_patient_id`).
- Inheritance: shared behavior is defined in parent classes (`Person`, `Patient`, `Doctor`).
- Polymorphism: `SpecialistDoctor.display_info()` overrides `Doctor.display_info()`.
- Abstraction: `Patient` defines an abstract billing interface via `calculate_bill()`.
- Composition: `Hospital` composes `Patient`, `Doctor`, `Appointment`, and `Prescription` objects.

## Added Features

- Appointment model using a dedicated `Appointment` class instead of tuples.
- Prescription model using a dedicated `Prescription` class.
- Specialist doctors with additional specialization and consultation fee.
- JSON persistence for patients, doctors, appointments, and prescriptions.
- Automatic load/save behavior in `Hospital`.
- Maintained existing menu flow and billing calculations.
