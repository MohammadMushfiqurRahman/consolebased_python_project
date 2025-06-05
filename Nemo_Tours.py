# Author:  Mohamma Mushfiqur Rahmann
# Student ID: 
# File: nemo_tours.py
# Date: 2025-05-06
# Purpose: Menu-driven application to manage tour bookings for Nemo Reef Tours.
# Features include entering bookings, displaying data/statistics, searching,
# saving/loading from CSV, with validation and formatted output.

import os

# Constants for menu options
ENTER_BOOKING = 1
DISPLAY_BOOKINGS = 2
DISPLAY_STATISTICS = 3
SEARCH_BOOKINGS = 4
SAVE_BOOKINGS = 5
READ_BOOKINGS = 6
EXIT = 7

# Constant for passenger charge
PASSENGER_CHARGE = 95.50

# Global variables to store bookings and track count
booking_names = []
booking_passengers = []
booking_count = 0

# Prints the column headings for bookings display
def print_heading():
    print("{:30s}{:11s}{:6s}".format("Booking name", "Passengers", "Charge"))

# Displays the menu options and validates user input
def get_menu_item():
    print("\nPlease select from the following")
    print(str(ENTER_BOOKING) + ". Enter booking name and number of passengers")
    print(str(DISPLAY_BOOKINGS) + ". Display all booking names, number of passengers and charges")
    print(str(DISPLAY_STATISTICS) + ". Display Statistics")
    print(str(SEARCH_BOOKINGS) + ". Search for booking")
    print(str(SAVE_BOOKINGS) + ". Save bookings to file")
    print(str(READ_BOOKINGS) + ". Read bookings from file")
    print(str(EXIT) + ". Exit the application")
    print("Enter choice==> ", end=" ")
    choice = input()
    while not choice.isdigit():
        print("Error - Menu selection must be numeric")
        print("Enter choice==> ", end=" ")
        choice = input()
    return int(choice)

# Processes the user's menu selection and routes to appropriate function
def process_menu_item():
    choice = get_menu_item()
    while choice != EXIT:
        if choice == ENTER_BOOKING:
            enter_booking()
        elif choice == DISPLAY_BOOKINGS:
            display_bookings()
        elif choice == DISPLAY_STATISTICS:
            display_statistics()
        elif choice == SEARCH_BOOKINGS:
            search_bookings()
        elif choice == SAVE_BOOKINGS:
            save_bookings()
        elif choice == READ_BOOKINGS:
            read_bookings()
        choice = get_menu_item()
    print("\nThank you for using the Nemo Reef Tours Management System\nProgram written by Mushfiqur\n")

# Validates that the entered booking name is not blank
def validate_booking_name():
    name = input("Enter booking name ==> ").strip()
    while name == "":
        print("Error - booking name cannot be blank")
        name = input("Enter booking name ==> ").strip()
    return name

# Validates that passenger input is numeric and at least 1
def validate_passenger_count(name):
    passengers = input("Enter number of passengers for " + name + " ==> ")
    while not passengers.isdigit() or int(passengers) < 1:
        print("ERROR must be numeric and number of passengers must be greater than or equal to one")
        passengers = input("Enter number of passengers for " + name + " ==> ")
    return int(passengers)

# Calculates total tour charge with applicable discounts
def calculate_charge(passengers):
    charge = passengers * PASSENGER_CHARGE
    if 3 <= passengers <= 5:
        charge *= 0.90
    elif 6 <= passengers <= 10:
        charge *= 0.85
    elif passengers > 10:
        charge *= 0.80
    return charge

# Prints a formatted booking receipt
def print_receipt(name, passengers, charge):
    print("\n\n---Nemo Tours Receipt---")
    print("Booking name:", name)
    print("Number of passengers:", passengers)
    print("Total Charge: $" + format(charge, ".2f"))

# Orchestrates booking entry, validation, and receipt display
def enter_booking():
    global booking_count
    name = validate_booking_name()
    passengers = validate_passenger_count(name)
    charge = calculate_charge(passengers)
    booking_names.append(name)
    booking_passengers.append(passengers)
    booking_count += 1
    print_receipt(name, passengers, charge)

# Displays all entered bookings in tabular format
def display_bookings():
    if booking_count == 0:
        print("ERROR please enter at least one booking")
        return
    print_heading()
    for i in range(booking_count):
        charge = calculate_charge(booking_passengers[i])
        print("{:30s}{:<11d}${:4.2f}".format(booking_names[i], booking_passengers[i], charge))

# Displays statistics: max/min passengers, average, total charge
def display_statistics():
    if booking_count == 0:
        print("ERROR please enter at least one booking")
        return
    max_pass = -1
    min_pass = 9999
    total_pass = 0
    total_charge = 0.0
    max_name = ""
    min_name = ""
    for i in range(booking_count):
        passengers = booking_passengers[i]
        name = booking_names[i]
        total_pass += passengers
        charge = calculate_charge(passengers)
        total_charge += charge
        if passengers > max_pass:
            max_pass = passengers
            max_name = name
        if passengers < min_pass:
            min_pass = passengers
            min_name = name
    avg_pass = total_pass / booking_count
    print("\nStatistics for Nemo Reef Tours")
    print(f"{max_name} has the maximum number of {max_pass} passengers")
    print(f"{min_name} has the maximum number of {min_pass} passengers")
    print("Average number of passengers per booking is {:.2f}".format(avg_pass))
    print("The Total charges are: ${:.2f}".format(total_charge))

# Performs case-insensitive search for a booking name
def search_bookings():
    if booking_count == 0:
        print("ERROR please enter at least one booking")
        return
    key = input("Enter booking name to search ==> ").lower().strip()
    found = False
    for i in range(booking_count):
        if booking_names[i].lower() == key:
            print("\nBooking found")
            print_heading()
            charge = calculate_charge(booking_passengers[i])
            print("{:30s}{:<11d}${:4.2f}".format(booking_names[i], booking_passengers[i], charge))
            found = True
            break
    if not found:
        print(key + " not found")

# Saves all bookings to a CSV file
def save_bookings():
    with open("bookings.csv", "w") as f:
        for i in range(booking_count):
            f.write(booking_names[i] + "," + str(booking_passengers[i]) + "\n")
    print("Data successfully saved to file")

# Reads booking data from CSV and appends to current data
def read_bookings():
    global booking_count
    if not os.path.exists("bookings.csv"):
        print("Error – file does not exist")
        return
    with open("bookings.csv", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                booking_names.append(parts[0])
                booking_passengers.append(int(parts[1]))
                booking_count += 1
    print("Data successfully read from the file")

# Entry point of the program
print("Welcome to the Nemo Reef Tours Management System")
process_menu_item()
