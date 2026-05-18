# ── Constants ──────────────────────────────────────────────────────────────────
BASE_CONSULTATION_FEE = 100
LAB_TEST_RATE = 10
SUBSIDY_RATE = 0.70


# ── Function 1: Register Patient ───────────────────────────────────────────────
def register_patient():
    while True:
        while True:
            name = input("Enter patient name: ")
            if name.strip() == "":
                print("Invalid name. Please enter a name.")
            else:
                break

        while True:
            try:
                age = int(input("Enter patient age: "))
                if age < 0:
                    print("Invalid age. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number for age.")

        while True:
            identification = input("Enter patient ID: ")
            if identification.strip() == "":
                print("Invalid ID. Please enter a patient ID.")
            else:
                break

        print(f"Patient: {name}, Age: {age}, ID: {identification} - Your registration is confirmed!")

        while True:
            option = input("Do you want to register another patient? (Yes/No): ").lower()
            if option == "yes" or option == "no":
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
        if option == "no":
            print("Thank you for registering the patient.")
            break


# ── Function 2: Book Appointment ───────────────────────────────────────────────
def book_appointment():
    from datetime import date, timedelta

    print("Departments:")
    print("1. GP")
    print("2. Specialist")

    while True:
        dept_choice = input("Please select a department (1 or 2): ").strip()
        if dept_choice == "1":
            department = "GP"
            print("You have selected GP")
            break
        elif dept_choice == "2":
            department = "Specialist"
            print("You have selected Specialist")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    today = date.today()
    min_date = today + timedelta(days=7)

    while True:
        date_input = input("Please enter your appointment date (YYYY-MM-DD): ").strip()

        parts = date_input.split("-")

        if len(parts) != 3:
            print("Invalid format. Please use YYYY-MM-DD (e.g. 2026-06-01).")
            continue
        try:
            user_year = int(parts[0])
            user_month = int(parts[1])
            user_day = int(parts[2])
            entered_date = date(user_year, user_month, user_day)
        except ValueError:
            print("Invalid date. Please enter a real date (month must be 1-12, day must be valid for that month).")
            continue

        if entered_date > min_date:
            print(f"Valid date. Your appointment date will be on: {date_input}")
            break
        else:
            print(f"Invalid. Date must be more than 7 days from today ({min_date}).")

    print("Booking Confirmed!")
    print(f"Department: {department}")
    print(f"Appointment Date: {date_input}")


# ── Function 3: Calculate Bill ─────────────────────────────────────────────────
def calculate_bill():
    print("===== Calculate Bill =====")

    patient_type = ""
    while patient_type != "SUBSIDISED" and patient_type != "PRIVATE":
        patient_type = input("Enter patient type (Subsidised / Private): ").strip().upper()
        if patient_type != "SUBSIDISED" and patient_type != "PRIVATE":
            print("Invalid input. Please enter 'Subsidised' or 'Private'.")

    lab_tests_input = ""
    while not lab_tests_input.isdigit():
        lab_tests_input = input("Enter number of lab tests completed: ")
        if not lab_tests_input.isdigit():
            print("Invalid input. Please enter a whole number (e.g. 0, 1, 2).")

    num_lab_tests = int(lab_tests_input)

    subtotal = BASE_CONSULTATION_FEE + (num_lab_tests * LAB_TEST_RATE)

    if patient_type == "SUBSIDISED":
        total = subtotal * SUBSIDY_RATE
    else:
        total = subtotal

    print("\n----- Bill Summary -----")
    print("Patient Type : " + patient_type.capitalize())
    print("Total Amount : $" + str(total))
    print("------------------------")


# ── Main Menu ──────────────────────────────────────────────────────────────────
while True:
    print("\n========================================")
    print("   CareBridge Hospital Management System")
    print("========================================")
    print("1. Register Patient")
    print("2. Book Appointment")
    print("3. Calculate Bill")
    print("4. Exit")
    print("========================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        register_patient()
    elif choice == "2":
        book_appointment()
    elif choice == "3":
        calculate_bill()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")