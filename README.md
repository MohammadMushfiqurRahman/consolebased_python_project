**Nemo Reef Tours Management System**

**Overview**
The Nemo Reef Tours Management System is a menu-driven Python application designed to manage tour bookings for Nemo Reef Tours. The program allows users to enter booking details, display booking information, view statistics, and search for specific bookings. Additionally, it supports saving and loading booking data to and from a CSV file.

**Features**
Enter Booking: Allows users to enter booking names and the number of passengers.

Display Bookings: Displays all bookings with the number of passengers and total charges.

Display Statistics: Shows booking statistics, including maximum, minimum, average number of passengers, and total charges.

Search Bookings: Allows users to search for a specific booking by name.

Save Bookings: Saves all bookings to a CSV file.

Read Bookings: Reads booking data from a CSV file and appends it to the current bookings.

**Menu Options**
Enter Booking: Enter a new booking name and the number of passengers.

Display Bookings: Display all bookings with passenger details and charges.

Display Statistics: Display statistics about the bookings (e.g., maximum, minimum passengers).

Search Bookings: Search for a booking by name.

Save Bookings: Save the current bookings to a CSV file.

Read Bookings: Load bookings from an existing CSV file.

Exit: Exit the program.

**How to Run**
Clone or download the repository.

Ensure you have Python installed (version 3.x recommended).

Open a terminal and navigate to the folder containing the Nemo_Tours.py file.

Run the program with the command:

python Nemo_Tours.py

**Code Structure**
Constants:

ENTER_BOOKING, DISPLAY_BOOKINGS, DISPLAY_STATISTICS, etc., represent the menu options.

PASSENGER_CHARGE is the base charge per passenger for the tour.

Global Variables:

booking_names: List of all booking names.

booking_passengers: List of the number of passengers for each booking.

booking_count: Counter tracking the total number of bookings.

**Functions:**

print_heading(): Prints column headings for displaying booking data.

get_menu_item(): Displays the menu and validates user input.

process_menu_item(): Processes the user's choice and routes to the corresponding function.

validate_booking_name(): Ensures the booking name is not blank.

validate_passenger_count(): Ensures the number of passengers is valid (greater than or equal to 1).

calculate_charge(): Calculates the total charge based on the number of passengers.

print_receipt(): Prints a formatted receipt for the booking.

enter_booking(): Handles the process of entering a new booking.

display_bookings(): Displays all current bookings.

display_statistics(): Displays statistics about the bookings.

search_bookings(): Searches for a booking by name.

save_bookings(): Saves all bookings to a CSV file.

read_bookings(): Reads bookings from a CSV file.

**Example Output**
Menu
Please select from the following

Enter booking name and number of passengers

Display all booking names, number of passengers and charges

Display Statistics

Search for booking

Save bookings to file

Read bookings from file

Exit the application
Enter choice==>

**Display Bookings**
Booking name Passengers Charge
Booking1 3 $286.50
Booking2 5 $477.50

**Display Statistics**
Statistics for Nemo Reef Tours
Booking1 has the maximum number of 5 passengers
Booking2 has the minimum number of 3 passengers
Average number of passengers per booking is 4.00
The Total charges are: $764.00

Receipt
---Nemo Tours Receipt---
Booking name: Booking1
Number of passengers: 5
Total Charge: $477.50

**Dependencies**
Python 3.x or higher

**License*
This project is open-source and available under the MIT License.
