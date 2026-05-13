

while True: 
    while True:
        name = input("Enter patient name: ")
        if name.strip() == "":
            print("Invalid name. Please enter a non-empty name.")
        else:
            break   

    while True:
        try: 
            age = int(input("Enter patient age: "))
            if age < 0:
                print("Invalid age. Please re enter age")
            break
        except ValueError:
            print("Please enter numbers")
        
        

    identification = input("Enter patient ID: ")  
    print(f"Patient: {name}, Age: {age}, ID: {identification} - Your registration is confirmed!")

 
    option = input("Do you want to register another patient? (Yes/No): ")
    if option == "No":
        print("Thank you for registering the patient")
        break




