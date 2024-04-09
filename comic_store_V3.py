class Comic:
    def __init__(self, comic_name, num_of_copies, note, total_sold):
        self.comic_name = comic_name
        self.num_of_copies = num_of_copies
        self.note = note
        self.total_sold = total_sold
        comic_list.append(self)

    def display_info(self):
        line("-", 25)
        print("Name: ", self.comic_name)
        print("Number of copies: ", self.num_of_copies)
        print("Total sold: ", self.total_sold)
        print("Note: ", self.note)
        line("-", 25)


def line(symbol, length: int):
    print(symbol * length)


def change_note():
    for comic in comic_list:
        option = input(f"Enter the new Note for {comic.comic_name} or 'X' to "
                       f"go back: ").capitalize()
        if option == "X":
            pass
        else:
            comic.note = option


def find_comic():
    name = input("Enter the name of the comic you want: "
                 "").title()
    for comic in comic_list:
        if comic.comic_name == name:
            return comic
    print(f"There was no comic with the name {name}")


def sell_comic():
    comic_name = None  #
    while comic_name is None:
        comic_name: Comic = find_comic()
    while True:
        try:
            sell_amount = int(input(f"Enter the amount of "
                                    f"{comic_name.comic_name} Comics that have"
                                    f" been sold: "))
        except ValueError:
            print(f"Error: Value must be an integer\n")
        else:
            if sell_amount < 0:
                print(f"Error: Value must be an integer\n")
                continue
            if sell_amount > comic_name.num_of_copies:
                print(f"Error: Sell amount must not be greater than copies "
                      f"on hand ({comic_name.num_of_copies})\n")
                continue
            break
    comic_name.num_of_copies -= sell_amount
    comic_name.total_sold += sell_amount
    print(f"{sell_amount} copy(s) of {comic_name.comic_name} was sold")


def restock_comic():
    comic_name = None  #
    while comic_name is None:
        comic_name: Comic = find_comic()
    while True:
        try:
            restock_amount = int(input(f"Enter the amount of "
                                       f"{comic_name.comic_name} Comics that "
                                       f"have been restocked: "))
        except ValueError:
            print(f"Error: Value must be an integer\n")
        else:
            if restock_amount < 0:
                print(f"Error: Value must be an integer\n")
                continue
            break
    comic_name.num_of_copies += restock_amount
    print(f"{restock_amount} copy(s) of {comic_name.comic_name} was "
          f"restocked\n")


comic_list = []

# List of comics that are being sold
c1 = Comic("Super Dude", 8, "Best seller", 0)
c2 = Comic("Lizard Man", 12, "Purchase less of these", 0)
c3 = Comic("Water Woman", 3, "Popular in the last month", 0)
c4 = Comic("Floppy arm Ethan", 50, "Never sold a copy", 0)


userChoice = ""
print("Welcome")

while userChoice != "Q":
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
