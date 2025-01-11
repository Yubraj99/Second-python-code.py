import os
import shutil
from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # A dictionary that uses the room number as a key to store rooms
        self.allocations = {}  # Dictionary to keep track of room assignments
        self.filename = "NZSE YUBRAJ KHADKA_85002062.txt"  # The primary files used to store allocations

    def add_room(self):
        room_number = input("Enter the number of the room: ")
        if room_number not in self.rooms:
            room_type = input("Enter the types of the room(e.g., Single, Double, Suite): ")
            price = float(input("Enter the cost of the room: "))
            self.rooms[room_number] = {"Type": room_type, "cost": price, "Status": "Available"}
            print(f"Room {room_number} has been added sucessfully .")
        else:
            print("The room space is already there!")

    def delete_room(self):
        room_number = input("To remove, enter the room number: ")
        if room_number in self.rooms:
            del self.rooms[room_number]
            print(f"Room {room_number} has been deleted sucessfully.")
        else:
            print("No room was found!")

    def display_room_details(self):
        if not self.rooms:
            print("Not a single room is available.")
        else:
            for room, details in self.rooms.items():
                print(f"Room Number: {room}, Type: {details['Type']}, Price: {details['Price']}, Status: {details['Status']}")

    def allocate_room(self):
        customer_name = input("Enter the name of the customer: ")
        room_number = input("Enter the room number to assign: ")
        
        if room_number in self.rooms and self.rooms[room_number]["Status"] == "Available":
            self.rooms[room_number]["Status"] = "Occupied"
            self.allocations[room_number] = customer_name
            print(f"Room {room_number} allocated to {customer_name}.")
        else:
            print("The room is either nonexistent or unavailable.")

    def display_room_allocation_details(self):
        if not self.allocations:
            print("There are no rooms assigned.")
        else:
            for room, customer in self.allocations.items():
                print(f"Room {room} is allocated to {customer}.")

    def billing_and_deallocation(self):
        room_number = input("To bill, enter the room number: ")
        if room_number in self.allocations:
            customer = self.allocations[room_number]
            print(f"Billing {customer} for Room {room_number}.")
            print(f"Room Price: {self.rooms[room_number]['Price']}")
            self.rooms[room_number]["Status"] = "Available"
            del self.allocations[room_number]
            print(f"Room {room_number} is now deallocated.")
        else:
            print("There is no room or it is not assigned.")

    def save_room_allocations_to_file(self):
        try:
            with open(self.filename, "w") as file:
                if not self.allocations:
                    print("No room allotments to conserve.")
                else:
                    for room, customer in self.allocations.items():
                        file.write(f"Room {room} allocated to {customer}\n")
                    print(f"Room assigment are stored to {self.filename}.")
        except IOError as e:
            print(f"error saving the file: {e}")

    def show_room_allocations_from_file(self):
        try:
            if not os.path.exists(self.filename):
                print(f"{self.filename} .")
                return

            with open(self.filename, "r") as file:
                content = file.read()
                if content:
                    print("Room Allocations from File:")
                    print(content)
                else:
                    print("No room allocations in the file.")
        except IOError as e:
            print(f"Error reading file: {e}")

    def backup_file(self):
        try:
            if not os.path.exists(self.filename):
                print(f"{self.filename} does not exist. Cannot backup.")
                return

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"NZSE_850002062_Backup_{timestamp}.txt"
            shutil.copy(self.filename, backup_filename)

            print(f"Backup created: {backup_filename}")

            # Clear the contents of the original file
            open(self.filename, "w").close()
            print(f"Original file {self.filename} has been cleared.")
        except IOError as e:
            print(f"An error occurred during the backup process: {e}")

    def exit_application(self):
        print("Exiting the application.")
        exit()


def main():
    hotel_system = HotelManagementSystem()

    while True:
        print("\nLANGHAM HOTEL MANAGEMENT SYSTEM")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. Display Room Details")
        print("4. Allocate Room")
        print("5. Display Room Allocation Details")
        print("6. Billing & De-Allocation")
        print("7. Save Room Allocations to a File")
        print("8. Show Room Allocations from a File")
        print("9. Backup Room Allocations and Clear Original File")
        print("10. Exit Application")
        
        try:
            choice = int(input("Enter the number of your choice here: "))

            if choice == 1:
                hotel_system.add_room()
            elif choice == 2:
                hotel_system.delete_room()
            elif choice == 3:
                hotel_system.display_room_details()
            elif choice == 4:
                hotel_system.allocate_room()
            elif choice == 5:
                hotel_system.display_room_allocation_details()
            elif choice == 6:
                hotel_system.billing_and_deallocation()
            elif choice == 7:
                hotel_system.save_room_allocations_to_file()
            elif choice == 8:
                hotel_system.show_room_allocations_from_file()
            elif choice == 9:
                hotel_system.backup_file()
            elif choice == 10:
                hotel_system.exit_application()
            else:
                print("Incorrect Selection.A number between 1 to 10 must be entered.")
        except ValueError:
            print("The input is invalid.Enter a vaild number, Please")

if __name__ == "__main__":
    main()
