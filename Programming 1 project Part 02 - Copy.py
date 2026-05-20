while True:
    while True:
        name = input("Enter patient name: ")
        if name.strip() == "":
            print("Invalid name. Please enter a  name.")
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

    
    identification = input("Enter patient ID: ")

    
    print(f"Patient: {name}, Age: {age}, ID: {identification} - Your registration is confirmed!")

    
    option = input("Do you want to register another patient? (Yes/No): ").lower()
    if option == "no":
        print("Thank you for registering the patient")
        break


department = """GP or Specialist"""
print(department)

while True:
    department2 = input("Please enter a department: ")
    department2 = department2.strip().upper()
    if department2 == 'GP':
        print("You have selected GP")
        print("Please enter a dateline one week after this date")
        break
    elif department2 == 'SPECIALIST':
        print("You have selected Specialist")
        print("Please enter a dateline one week after this date")
        break
    else:
        print("Invalid department, please re-enter a valid one")

while True:
    date_input = input("Please enter your appointment date (YYYY-MM-DD): ")
    
    parts = date_input.split("-")
    
    if len(parts) != 3:
        print("Invalid, please use YYYY-MM-DD")
        continue
    try:
        user_year = int(parts[0])
        user_month = int(parts[1])
        user_day = int(parts[2])
    except ValueError:
        print("Invalid, please use YYYY-MM-DD")
        continue

    min_year = 2026
    min_month = 5
    min_day = 24
    

    if user_year > min_year:
        print(f"Valid date. Your appointment date will be on: {date_input}")
        break
    elif user_year == min_year:
        if user_month > min_month:
            print(f"Valid date. Your appointment date will be on: {date_input}")
            break
        elif user_month == min_month:
            if user_day >= min_day:
                print(f"Valid date. Your appointment date will be on: {date_input}")
                break
            else:
                print(f"Invalid, Date must be after {min_year}-{min_month}-{min_day}")
        else:
            print(f"Invalid, Date must be after {min_year}-{min_month}-{min_day}")
    else:
        print(f"Invalid, Date must be after {min_year}-{min_month}-{min_day}")

print("Booking Confirmed!")
print(f"Department: {department2}")
print(f"Appointment Date: {date_input}")