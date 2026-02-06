while True:
    print("\n--- NOKIA 3310 MENU ---")
    print("1. Phonebook")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call Divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminder")
    print("11. Profiles")
    print("12. SIM Services")
    print("0. Exit")

    menu = input("Select Menu option: ")

    match menu:
        case "1":
            while True:
                print("\n--- PHONEBOOK ---")
                print("1. Search")
                print("2. Add Name")
                print("3. Edit")
                print("4. Erase")
                print("0. Back")

                opt = input("Select option: ")
                if opt == "0":
                    break
                else:
                    print("Processing...")

        case "2":
            while True:
                print("\n--- MESSAGES ---")
                print("1. Write Message")
                print("2. Inbox")
                print("3. Outbox")
                print("0. Back")

                opt = input("Select option: ")
                if opt == "0":
                    break
                else:
                    print("Opening message...")

        case "3":
            print("Opening Chat...")

        case "4":
            while True:
                print("\n--- CALL REGISTER ---")
                print("1. Missed Calls")
                print("2. Received Calls")
                print("3. Dialled Numbers")
                print("0. Back")

                opt = input("Select option: ")
                if opt == "0":
                    break
                else:
                    print("Loading call records...")

        case "5":
            print("Opening Tones...")

        case "6":
            while True:
                print("\n--- SETTINGS ---")
                print("1. Call Settings")
                print("2. Phone Settings")
                print("3. Security Settings")
                print("4. Restore Factory Settings")
                print("0. Back")

                settings = input("Select option: ")

                match settings:
                    case "1":
                        while True:
                            print("\n--- CALL SETTINGS ---")
                            print("1. Automatic Redial")
                            print("2. Speed Dialling")
                            print("0. Back")

                            opt = input("Select option: ")
                            if opt == "0":
                                break
                            else:
                                print("Setting saved")

                    case "2":
                        while True:
                            print("\n--- PHONE SETTINGS ---")
                            print("1. Language")
                            print("2. Display")
                            print("0. Back")

                            opt = input("Select option: ")
                            if opt == "0":
                                break
                            else:
                                print("Setting saved")

                    case "3":
                        while True:
                            print("\n--- SECURITY SETTINGS ---")
                            print("1. PIN Code")
                            print("2. Call Barring")
                            print("0. Back")

                            opt = input("Select option: ")
                            if opt == "0":
                                break
                            else:
                                print("Setting saved")

                    case "4":
                        print("Restoring factory settings...")

                    case "0":
                        break

                    case _:
                        print("Invalid option")

        case "7":
            print("Call Divert activated")

        case "8":
            print("Opening Games...")

        case "9":
            print("Opening Calculator...")

        case "10":
            print("No reminders set")

        case "11":
            print("Opening Profiles...")

        case "12":
            print("Accessing SIM Services...")

        case "0":
            print("Exiting Nokia Menu...")
            break

        case _:
            print("Invalid menu option")
