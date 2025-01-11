class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # A dictionary that uses the room number as a 
        self.allocations = {}  # A dictionary that uses the room number as a key to store rooms

    def add_room(self):
        room_number = input("Enter the number of the room: ")
        if room_number not in self.rooms:
            room_type = input("Enter the type of room (e.g., suite, double, or single).: ")
            price = float(input("Enter the cost of the room: "))
            self.rooms[room_number] = {"Type": room_type, "Price": price, "Status": "Available"}
            print(f"Room {room_number} added successfully.")
        else:
            print("There is already space!")

    def delete_room(self):
        room_number = input(" To remove,enter the room number: ")
        if room_number in self.rooms:
            del self.rooms[room_number]
            print(f"Room {room_number} has been successfully deleted.")
        else:
            print("No room was found!")

    def display_room_details(self):
        if not self.rooms:
            print("No rooms are available.")
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
            print("No room is allotted or exists.")

    def exit_application(self):
        print("leaving the application.")
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
        print("7. Exit Application")
        
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
                hotel_system.exit_application()
            else:
                print("Incorrect selection.Enter a number from 1 to 7 Please.") 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
