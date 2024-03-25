import datetime

from utils.event_manager import EventScheduler
from utils.utils import get_date_input


def main():
    scheduler = EventScheduler()

    while True:
        print("\nOptions:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. List Events")
        print("4. Quit")

        choice = input("Type your choice then press enter: ")

        if choice == "1":
            title = input("Enter event title: ")

            if not title:
                print("Title cannot be empty.")

                continue

            date = get_date_input()
            description = input("Enter event description (optional): ")
            scheduler.add_event(title, date, description)
            print("Event added successfully.")
        elif choice == "2":

            event_list = scheduler.list_events()
            for index, event in enumerate(event_list):
                print(f"{index + 1}. {event}")

            title = input("Enter the title of the event to remove: ")

            if scheduler.remove_event(title):
                print("Event removed successfully.")
            else:
                print(f"No event with title {title} found.")
        elif choice == "3":
            scheduler.print_events()
        elif choice == "4":
            scheduler.save_events()
            print("Events saved successfully. Exiting... ")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
