# 🏥 CareBridge Hospital Management System

A command-line application built in Python that helps manage basic hospital operations — including patient registration, appointment booking, bill calculation, and triage room assignment.

---

## 📋 Table of Contents

- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Main Menu](#main-menu)
- [Features](#features)
  - [1. Register Patient](#1-register-patient)
  - [2. Book Appointment](#2-book-appointment)
  - [3. Calculate Bill](#3-calculate-bill)
  - [4. Assign Triage Room](#4-assign-triage-room)
  - [5. Exit](#5-exit)
- [Billing Rates](#billing-rates)
- [Notes](#notes)

---

## Requirements

- **Python 3.x** (any version of Python 3 will work)
- No external libraries needed — only Python's built-in `datetime` module is used

To check if Python is installed, open your terminal or command prompt and run:

```
python --version
```

If Python is not installed, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## How to Run

1. Download or clone this repository to your computer
2. Open a terminal (Mac/Linux) or Command Prompt (Windows)
3. Navigate to the folder containing the file:

```
cd path/to/your/folder
```

4. Run the program:

```
python "Full finished version of  group project for PG1 (5).py"
```

The main menu will appear and the program will guide you from there.

---

## Main Menu

When the program starts, you will see:

```
========================================
   CareBridge Hospital Management System
========================================
1. Register Patient
2. Book Appointment
3. Calculate Bill
4. Assign Triage Room
5. Exit

Enter your choice (1-5):
```

Type a number from **1 to 5** and press **Enter** to select an option.

---

## Features

### 1. Register Patient

Registers a new patient into the system.

**You will be asked to enter:**
- Patient name (cannot be blank)
- Patient age (must be a whole number, 0 or above)
- Patient ID (cannot be blank)

Once all details are entered, the system will confirm registration. You will then be asked if you want to register another patient — enter `Yes` or `No`.

**Example:**
```
Enter patient name: John Tan
Enter patient age: 45
Enter patient ID: P10234
Patient: John Tan, Age: 45, ID: P10234 - Your registration is confirmed!
Do you want to register another patient? (Yes/No): No
Thank you for registering the patient.
```

---

### 2. Book Appointment

Books an appointment for a patient in a selected department.

**Step 1 — Select a department:**

```
Departments:
1. GP
2. Specialist
```

Enter `1` for General Practitioner or `2` for Specialist.

**Step 2 — Enter an appointment date:**

- Format: `YYYY-MM-DD` (e.g. `2026-07-01`)
- The date must be **more than 7 days from today**
- The date must be a real, valid calendar date

**Example:**
```
Please select a department (1 or 2): 1
Please enter your appointment date (YYYY-MM-DD): 2026-07-15
Valid date. Your appointment date will be on: 2026-07-15
Booking Confirmed!
Department: GP
Appointment Date: 2026-07-15
```

---

### 3. Calculate Bill

Calculates the total bill for a patient based on their type and number of lab tests.

**You will be asked to enter:**
- Patient type: `Subsidised` or `Private`
- Number of lab tests completed (whole number, e.g. `0`, `1`, `2`)

**How the bill is calculated:**

| Item | Rate |
|---|---|
| Base consultation fee | $100 |
| Each lab test | $10 |
| Subsidised discount | 30% off the subtotal |

**Example:**
```
Enter patient type (Subsidised / Private): Subsidised
Enter number of lab tests completed: 3
```

```
----- Bill Summary -----
Patient Type : Subsidised
Total Amount : $91.0
------------------------
```

> **Calculation:** (100 + 3 × 10) × 0.70 = $91.00

---

### 4. Assign Triage Room

Assigns a patient to a room based on the severity of their condition.

**You will be asked to enter:**
- Severity level: a whole number from **1 to 10**

**Room assignment rules:**

| Severity | Assigned Room |
|---|---|
| 1 – 4 | Waiting Room |
| 5 – 7 | Room 1 |
| 8 – 10 | Room 2 |

**Example:**
```
Enter severity of condition (1-10): 6
```

```
--- Triage Summary ---
Severity Level: 6
Assigned Room: Room 1
```

---

### 5. Exit

Exits the program.

```
Program exited. Thank you
```

---

## Billing Rates

For reference, here are the fixed rates used in billing:

| Constant | Value |
|---|---|
| Base Consultation Fee | $100 |
| Lab Test Rate (per test) | $10 |
| Subsidy Rate (Subsidised patients pay) | 70% of subtotal |

---

## Notes

- All inputs are validated — the program will prompt you again if you enter something invalid
- The program runs in a loop until you select **Exit (option 5)**
- Appointment dates must use the format `YYYY-MM-DD` exactly
- Patient type input for billing is not case-sensitive (`subsidised`, `SUBSIDISED`, and `Subsidised` are all accepted)
