class Comic:
    def __init__(self, comic_name, num_of_copies, note):
        self.comic_name = comic_name
        self.num_of_copies = num_of_copies
        self.note = note
        comic_list.append(self)

    def display_info(self):
        line("-", 25)
        print("Name: ", self.comic_name)
        print("Number of copies: ", self.num_of_copies)
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
c1 = Comic("Super Dude", 8, "Best seller")
c2 = Comic("Lizard Man", 12, "Purchase less of these")
c3 = Comic("Water Woman", 3, "Popular in the last month")
c4 = Comic("Floppy arm Ethan", 50, "Never sold a copy")

sell_comic()
for comic in comic_list:
    comic.display_info()
