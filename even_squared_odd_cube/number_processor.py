class NumberProcessor :
    def __init__(self, number):
        self.number = number

    def process_numbers(self, double_number, triple_number):
        try:
            with open(self.number, "r") as numbers_file :
                number = numbers_file.read().split()

            with open(double_number, 'w') as double_numbers_file :
                with open(triple_number, 'w') as triple_numbers_file :

                    for num in number:
                        num = num.strip()
                        num = int(num)

                        if num % 2 == 0:
                            double_numbers_file.write(f"{num} = {str(num ** 2)}\n")
                        else:
                            triple_numbers_file.write(f"{num} = {str(num ** 3)}\n")
            print('Files Created Successfully')
        except FileNotFoundError :
            print('Error: File Not Found')
        except ValueError :
            print('Error: Invalid Number in file')

