def assign_triage_room():
    while True:
        severity_input = input("Enter severity of condition (1-10): ").strip()

        if not severity_input.isdigit():
            print("Error: Severity must be a whole number.")
            continue

        severity = int(severity_input)

        if severity < 1 or severity > 10:
            print("Error: Severity must be between 1 and 10.")
            continue

        # Assign room based on severity
        if 1 <= severity <= 4:
            room = "Waiting Room"
        elif 5 <= severity <= 7:
            room = "Room 1"
        else:
            room = "Room 2"

        print("\n--- Triage Summary ---")
        print(f"Severity Level: {severity}")
        print(f"Assigned Room: {room}\n")
        break

assign_triage_room()



