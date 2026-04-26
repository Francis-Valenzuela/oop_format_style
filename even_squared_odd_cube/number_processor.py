class NumberProcessor :
    def __init__(self, number):
        self.number = number

    def process_numbers(self, double_number, triple_number):
        with open(self.number, "r") as numbers_file :
            number = numbers_file.readlines()

            for num in number :
                num = num.strip()
                num = int(num)
        with open(double_number, 'w') as double_numbers_file :
            with open(triple_number, 'w') as triple_numbers_file :
                if num % 2 == 0
                    double_numbers_file.write(str(num ** 2) + '\n')
                else:
                    triple_numbers_file.write(str(num ** 3) + '\n')

