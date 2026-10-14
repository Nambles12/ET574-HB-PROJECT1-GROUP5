# main.py
#import tracker  # This connects to the file your teammates will build

def main():
    while True:
        # The exact menu text requested by Prof. Sun
        print("\nWelcome to Study Session Tracker!")
        print("1. Add Study Session")
        print("2. View Summary")
        print("3. View All Sessions")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        # Program logic and module integration
        if choice == '1':
            # This will call Student B's function once they finish it
            # tracker.add_session()
            print("Add session feature coming soon!")
        elif choice == '2':
            # This will call Student C's function once they finish it
            # tracker.view_summary()
            print("Summary feature coming soon!")
        elif choice == '3':
            # This will call Student C's function once they finish it
            # tracker.view_all()
            print("View all feature coming soon!")
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()