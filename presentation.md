---
marp: true
theme: default
paginate: true
---

# Medical Diagnosis System
**Project Presentation**

---

## Introduction

The Medical Diagnosis System is a software application developed to assist in identifying diseases based on symptoms provided by users. The system uses Python for processing and SQL for storing patient and diagnosis data securely. It helps improve healthcare efficiency and provides quick preliminary diagnosis support.

---

## Objectives of the Project

- To automate basic medical diagnosis.
- To store patient records securely.
- To reduce manual diagnosis efforts.
- To provide quick symptom analysis.
- To generate patient diagnosis reports.

---

## Problem Statement

Traditional diagnosis systems require manual record maintenance and may consume more time in analyzing symptoms. Maintaining patient records manually can lead to errors and data loss. This project solves these problems using Python and SQL for efficient diagnosis management.

---

## Technologies Used

**Programming Language**
- Python

**Database**
- MySQL / SQLite

**Python Libraries**
- Tkinter
- Pandas
- `mysql.connector`
- Datetime Module

**Tools**
- VS Code / PyCharm
- MySQL Workbench

---

## System Architecture

**Modules:**
- Patient Module
- Doctor/Admin Module
- Diagnosis Module
- Database Module
- Report Module

**Workflow:**
`User Registration/Login` $\rightarrow$ `Symptom Entry` $\rightarrow$ `Disease Analysis` $\rightarrow$ `Database Storage` $\rightarrow$ `Report Generation`

---

## Features of the System

- Patient registration and login
- Symptom-based disease prediction
- Secure patient data storage
- Quick diagnosis reports
- Doctor/admin management
- Easy data retrieval
- User-friendly interface

---

## Database Design

**Patient Table**
- Patient ID, Name, Age, Gender, Contact Details

**Diagnosis Table**
- Diagnosis ID, Patient ID, Symptoms, Predicted Disease, Date

**Doctor Table**
- Doctor ID, Name, Specialization, Contact Details

---

## Working Process

1. Patient registers into the system.
2. Symptoms are entered by the user.
3. Python processes the symptoms.
4. Possible disease is predicted.
5. Diagnosis details are stored in SQL database.
6. Reports are generated for future reference.

---

## Advantages

- Faster diagnosis process
- Reduces manual paperwork
- Improves data accuracy
- Secure patient record management
- Easy report generation
- Time-saving healthcare support

---

## Applications

- Hospitals
- Clinics
- Healthcare Centers
- Medical Research Systems
- Online Healthcare Platforms

---

## Future Enhancements

- AI-based disease prediction
- Integration with hospital management systems
- Cloud database support
- Mobile application support
- Real-time doctor consultation
- Voice-based symptom input

---

## Security Features

- User Authentication
- Secure SQL Database
- Password Protection
- Data Backup and Recovery
- Role-based Access Control

---

## Conclusion

The Medical Diagnosis System using Python and SQL provides a secure and efficient platform for symptom analysis and patient data management. It improves healthcare efficiency, reduces manual work, and supports faster diagnosis processes.
