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









def view_all():
    print("\n--- All Study Sessions ---")
    
    if len(data.subjects) == 0:
        print("No study sessions recorded yet.")
        return

    # Loops through the parallel lists to print each session
    for i in range(len(data.subjects)):
        print(f"Session {i + 1}:")
        print(f"  Subject:  {data.subjects[i]}")
        print(f"  Minutes:  {data.minutes[i]}")
        print(f"  Location: {data.locations[i]}")
        print(f"  Notes:    {data.notes[i]}")
        print("-" * 25)

def view_summary():
    print("\n--- Summary Report ---")
    total_sessions = len(data.minutes)
    
    if total_sessions == 0:
        print("No study sessions recorded yet.")
        return
        
    # Accurate calculations for the summary
    total_minutes = sum(data.minutes)
    avg_minutes = total_minutes / total_sessions
    longest_session = max(data.minutes)
    shortest_session = min(data.minutes)
    
    # Clear output formatting
    print(f"Total Sessions:           {total_sessions}")
    print(f"Total Minutes:            {total_minutes}")
    print(f"Average Minutes/Session:  {avg_minutes:.1f}")
    print(f"Longest Session:          {longest_session} minutes")
    print(f"Shortest Session:         {shortest_session} minutes")