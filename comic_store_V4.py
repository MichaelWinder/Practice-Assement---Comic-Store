import pickle


# Class of Comic
class Comic:
    def __init__(self, comic, num_of_copies, note, total_sold):
        self.comic = comic
        self.ori_num_of_copies = num_of_copies
        self.num_of_copies = num_of_copies
        self.note = note
        self.total_sold = total_sold

    # Displays all the information for the desired Comic
    def display_info(self):
        line("-", 25)
        print("Name: ", self.comic)
        print("Number of copies: ", self.num_of_copies)
        print("Total sold: ", self.total_sold)
        print("Note: ", self.note)
        line("-", 25)


# Sets up the global variable comic_list
def load_inventory(filename):
    try:  # Checks whether the pickle file exists
        with open(filename, "rb") as f:
            return pickle.load(f)  # Returns the saved comic list
    except FileNotFoundError:  # If not found sets comic_list to original
        # information
        return [Comic("Super Dude", 8, "Best seller", 0),
                Comic("Lizard Man", 12, "Purchase less of these", 0),
                Comic("Water Woman", 3, "Popular in the last month", 0),
                Comic("Floppy arm Ethan", 50, "Never sold a copy", 0)]


# (Creates and) Saves the changed comic stock to the pickle file
def save_inventory(filename):
    with open(filename, "wb") as f:
        pickle.dump(comic_list, f)


# Creates lines easier
def line(symbol, length: int):
    print(symbol * length)


# Changes the note within each comic
def change_note():
    for comic in comic_list:
        option = input(f"Enter the new Note for {comic.comic} or 'X' to "
                       f"go back: ").capitalize()
        if option == "X":
            pass
        else:
            comic.note = option


# Finds and returns a selected comic
def find_comic():
    name = input("Enter the name of the comic you want: ").title()
    for comic in comic_list:
        if comic.comic == name:  # Checks if typed name exists
            return comic
    print(f"There was no comic with the name {name}")


# Records the sale of a comic
def sell_comic():
    comic = None
    while comic is None:  # Loop to keep asking for comic input until a
        # valid one is given
        comic = find_comic()
    while True:  # Loop for error checking on the sell amount
        try:
            sell_amount = int(input(f"Enter the amount of "
                                    f"{comic.comic} Comics that have"
                                    f" been sold: "))
        except ValueError:  # If value isn't a number
            print(f"Error: Value must be an integer\n")
        else:
            if sell_amount < 0:  # If value is less the 0
                print(f"Error: Value must be greater than 0\n")
                continue
            if sell_amount > comic.num_of_copies:  # If value is greater
                # than comics stored in the inventory
                print(f"Error: Sell amount must not be greater than copies "
                      f"on hand ({comic.num_of_copies})\n")
                continue
            break
    comic.num_of_copies -= sell_amount  # Changes values once error checked
    comic.total_sold += sell_amount
    print(f"{sell_amount} copy(s) of {comic.comic} was sold")


# Records the restocking of a comic
def restock_comic():
    comic = None
    while comic is None:  # Loop to keep asking for comic input until a
        # valid one is given
        comic = find_comic()
    while True:  # Loop for error checking on the restock amount
        try:
            restock_amount = int(input(f"Enter the amount of "
                                       f"{comic.comic} Comics that "
                                       f"have been restocked: "))
        except ValueError:  # If value isn't a number
            print(f"Error: Value must be an integer\n")
        else:
            if restock_amount < 0:  # If value is less the 0
                print(f"Error: Value must be greater than 0\n")
                continue
            break
    comic.num_of_copies += restock_amount  # Changes values once error checked
    print(f"{restock_amount} copy(s) of {comic.comic} was "
          f"restocked\n")


# The menu hub where all other functions diverge from
def menu():
    userChoice = ""
    print("Welcome")
    while userChoice != "Q":  # Loop to keep asking questions
        print("What function would you like to run?")
        print("Type 1 to find a Comic")
        print("Type 2 to record a sale of a comic")
        print("Type 3 to record a restock of a comic")
        print("Type 4 to change the note of a comic")
        print("Type 5 to print all comic records and information")
        print("Type Q to quit")
        userChoice = input("Enter choice: ").upper()
        print()

        if userChoice == "1":
            find_comic()
        elif userChoice == "2":
            sell_comic()
        elif userChoice == "3":
            restock_comic()
        elif userChoice == "4":
            change_note()
        elif userChoice == "5":
            for comic in comic_list:
                comic.display_info()
        print()
    save_inventory("comic_store_inventory.txt")  # Saves the inventory at
    # the end of the program


# Main Routine
comic_list: list[Comic] = load_inventory("comic_store_inventory.txt")
# Runs load_inventory to create the comic list
menu()
