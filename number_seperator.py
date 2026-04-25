class NumberSeperator:
    def __init__(self, file):
        self.file = file

    def separate_numbers(self, even.file, odd_file):
        try:
           with open(self.file, 'r') as infile:
               numbers = infile.readlines()