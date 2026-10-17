import data

def add_session():
    print("add a study session")
    subject = input("enter subject/course: ")
    minutes_studied = input("how many minutes did you study? ")
    if not minutes_studied. isdigit() or int(minutes_studied) <= 0:
        print("invalid minutes. Please enter a positive number.")

        minutes_studied = int(minutes_studied)

    print("Choose a study location:")
    print("1. home")
    print("2. Library")
    print("3. Lab")
    print("4. Other")

    location = input("Enter your choice (1-4): ")
    if location not in ['1', '2', '3', '4']:
        print("invalid location choice.")
        return
        if location == "1":
            location = "home"
        elif location == "2":
            location = "library"
        elif location == "3":
            location = "lab"
        else:
            location = "other"
        data.subjects.append(subject)
        data.minutes.append(minutes_studied)
        data.locations.append(location)
        data.notes.append(notes)

        print("study session saved succesfully!")

    notes = input("Enter notes (optional): ")

