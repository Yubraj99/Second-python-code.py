#Name:Yubraj Khadka
#FileNAME: "NZSE_YUBRAJ_KHADKA_85002062.txt"
#Description : Appliation for "Langham Hotels"

#This Project on Hotel Management is a general software developed (inPython). To manage the workings of a hotel as to minimize or in fact eliminate the need for manpower. In this project,,HotelManagementSystem "Yubraj Khadka ” AnCasa” 
#Is the name of the hotel getting developed in the project. It embraces main essential areas of hotel management and this system
#Could do the following processes - Hotel Reservation, Offer you Hotel Rooms Information, Room Service, Account and Archives.

import os
import shutil
from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # A dictionary that uses the room number as a key to store rooms.It helps to keep data save and store the occpancy of the room.
        self.allocations = {}  # Dictionary to keep track of room assignments. It helps to list and indetify the data.
        self.filename = ".txt"  # File used to store allocations

    def add_room(self):
        try:
            room_number = input("Enter the number of the room: ")
            if room_number not in self.rooms:
                room_type = input("Enter the type of the room (e.g., Single, Double, Suite): ")
                price = float(input("Enter the cost of the room: "))
                self.rooms[room_number] = {"Type": room_type, "cost": price, "Status": "Available"}
                print(f"Room {room_number} has been added successfully.")
            else:
                print("The room already exists!")
        except ValueError:
            print("Invalid input. Please enter numeric values for room price.")

    def delete_room(self):
        try:
            room_number = input("To remove, enter the room number: ")# Remove room print the message
            if room_number in self.rooms:
                del self.rooms[room_number]
                print(f"Room {room_number} has been deleted successfully.")
            else:
                print("Room not found!")
        except Exception as e:
            print(f"An error occurred: {"Room not found."}")

    def display_room_details(self): # It display the room details.
        try:
            if not self.rooms:
                print("No rooms are available.")
            else:
                for room, details in self.rooms.items():
                    print(f"Room Number: {room}, Type: {details['Type']}, Price: {details['cost']}, Status: {details['Status']}")
        except KeyError as e:
            print(f"Data error: {e}. Check room details.")

    def allocate_room(self):
        try:
            customer_name = input("Enter the name of the customer: ")
            room_number = input("Enter the room number to assign: ")

            if room_number in self.rooms:
                if self.rooms[room_number]["Status"] == "Available":
                    self.rooms[room_number]["Status"] = "Occupied"
                    self.allocations[room_number] = customer_name
                    print(f"Room {room_number} allocated to {customer_name}.")
                else:
                    print("The room is already occupied.")
            else:
                print("Room does not exist.")
        except KeyError as e:
            print(f"Error in data handling: {e}")

    def display_room_allocation_details(self): # It display the room location details.
        try:
            if not self.allocations:
                print("No rooms are currently assigned.")
            else:
                for room, customer in self.allocations.items():
                    print(f"Room {room} is allocated to {customer}.")
        except IndexError:
            print("Allocation data is out of range.")

    def billing_and_deallocation(self): #It display the billing and deallocation.
        try:
            room_number = input("Enter the room number for billing: ")
            if room_number in self.allocations:
                customer = self.allocations[room_number]
                print(f"Billing {customer} for Room {room_number}.")
                print(f"Room Price: {self.rooms[room_number]['cost']}")
                self.rooms[room_number]["Status"] = "Available"
                del self.allocations[room_number]
                print(f"Room {room_number} is now deallocated.")
            else:
                print("The room is either unassigned or does not exist.")
        except KeyError as e:
            print(f"Key Error in accessing room details: {e}")

    def save_room_allocations_to_file(self): #It display the save room allocation files.
        try:
            with open(self.filename, "w") as file:
                if not self.allocations:
                    print("No room allocations to save.")
                else:
                    for room, customer in self.allocations.items():
                        file.write(f"Room {room} allocated to {customer}\n")
                    print(f"Room allocations saved to {self.filename}.")
        except IOError as e:
            print(f"File saving error: {e}")

    def show_room_allocations_from_file(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"File {self.filename} does not exist.")
            with open(self.filename, "r") as file:
                content = file.read()
                if content:
                    print("Room Allocations from File:")
                    print(content)
                else:
                    print("No room allocations found in the file.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except IOError as e:
            print(f"File reading error: {e}")

    def backup_file(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"{self.filename} does not exist. Cannot backup.")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"NZSE_85002062_Backup_{timestamp}.txt"
            shutil.copy(self.filename, backup_filename)
            print(f"Backup created: {backup_filename}")
            open(self.filename, "w").close()
            print(f"Original file {self.filename} has been cleared.")
        except FileNotFoundError as e:
            print(f"File Not Found Error: {e}")
        except IOError as e:
            print(f"Backup process error: {"File Not Found error"}")

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
            choice = int(input("Enter your choice: "))
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
                print("Invalid choice. Please select between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()

        
           
          
      
               
