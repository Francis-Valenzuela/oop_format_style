class NumberProcessor :
    def __init__(self, number):
        self.number = number

    def process_numbers(self, double_number, triple_number):
        with open(self.number, "r") as numbers_file :
            number = numbers_file.readlines()

            for num in number :
                num = num.strip()
                num = int(num)

