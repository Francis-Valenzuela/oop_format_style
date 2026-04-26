class TextFileWriter:
    def __init__(self, filename):
        self.filename = filename

    def w_lines(self):
        try:
            with open(self.filename, 'w') as file:
                while True:
                    line = input("Enter a line to write: ")
                    file.write(line + '\n')

                    choice = input("Would you like to add another line? (y/n): ").lower()
                    while choice not in ['y', 'n']:
                        choice = input("Please enter 'y' or 'n':")

                    if choice != 'y':
                        break

        except ValueError:
            print("Invalid Value")
