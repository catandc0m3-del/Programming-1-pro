while True:
    while True:
        name = input("Enter patient name: ")
        if name.strip() == "":
            print("Invalid name. Please enter a  name.")
        else:
            break   

    identification = None
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
        if identification.strip() == "":
            print("Please enter Patient ID:   ")

    
    print(f"Patient: {name}, Age: {age}, ID: {identification} - Your registration is confirmed!")

    
    option = input("Do you want to register another patient? (Yes/No): ").lower()
    if option == "no":
        print("Thank you for registering the patient")
        break
