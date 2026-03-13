# Import the necessary modules
import random
from datetime import date
  
# Create a constant for the name of the text file
QUOTATIONS_FILE = "quotations.txt"
  
# This function displays the app menu
def show_menu():
    print("\nWelcome to the Quotations Archive!\n")
    print("What would you like to do?")
    print("1. View all quotations")
    print("2. Add a new quotation")
    print("3. Get a random quotation")
    print("4. Quit")
  
# This function reads the quotations from the file
# and returns them as a list
def read_quotations():
    # Start with an empty list
    quotations = []
  
    # Check if the file exists before trying to read it
    if not file_exists(QUOTATIONS_FILE):
        # If the file doesn't exist, return an empty list
        return quotations
  
    # Open the file in read mode
    with open(QUOTATIONS_FILE, "r") as file:
        # Read each line from the file
        for line in file:
            # Strip whitespace and add the line to the list
            quotations.append(line.strip())
  
    # Return the list of quotations
    return quotations
  
# This function checks if the file exists
# and returns True or False
def file_exists(filename):
  
    # Import the os module to check for file existence
    import os
  
    # Use os.path.exists to check if the file exists
    # and return the result
    return os.path.exists(filename)
  
# This function saves a new quotation to the file
def save_quotation(quotation):
    # Open the file in append mode
    with open(QUOTATIONS_FILE, "a") as file:
  
        # Get the current date and format it
        # and format it as YYYY-MM-DD
        today = date.today().isoformat()
  
        # Write the quotation and the date to the file
        file.write(f"{quotation} (added on {today})\n")
  
# This function asks for a new quotation        
def add_new_quotation():
  
    # Prompt the user for a new quotation
    quotation = input("Enter your quotation: ")
  
    # Save the quotation to the file
    save_quotation(quotation)
  
    # Inform the user that it has been saved
    print("Quotation saved!")
  
# This function displays all saved quotations
def view_all_quotations():
  
    # Read the quotations from the file
    quotations = read_quotations()
  
    # Check if there are any quotations
    if not quotations:
        # If not, inform the user
        print("No quotations saved yet.")
    else:
        # If there are, display them
        print("\nYour saved quotations:")
        for quotation in quotations:
            print(f"- {quotation}")
  
# This function displays a random quotation
def show_random_quotation():
    # Read the quotations from the file
    quotations = read_quotations()
  
    # Check if there are any quotations
    if not quotations:
        # If not, inform the user
        print("No quotations to show. Try adding some first!")
    else:
        # If there are, choose one at random
        # and display it
        print("\nHere's a random quotation:")
        print(random.choice(quotations))
  
# This function is the main loop of the program
def main():
    # Loop until the user chooses to quit
    while True:
  
        # Show the menu and get the user's choice
        show_menu()
        choice = input("Choose an option (1-4): ")
  
        # Check the user's choice,
        # then call the appropriate function
        if choice == "1":
            # Display all the quotations
            view_all_quotations()
        elif choice == "2":
            # Prompt for a new quotation
            add_new_quotation()
        elif choice == "3":
            # Display a random quotation
            show_random_quotation()
        elif choice == "4":
            # Exit the program
            print("Goodbye! Keep those quotations coming.")
            # Exit the loop to quit the program
            break
        else:
            # Handle a choice that's not 1-4
            print("Invalid option. Please try again.")
  
# Run the main function to start the program
main()
