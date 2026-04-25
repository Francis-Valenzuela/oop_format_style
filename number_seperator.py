class NumberSeperator:
    def __init__(self, file):
        self.file = file

    def separate_numbers(self, even_file, odd_file):
        try:
           with open(self.file, 'r') as input_file:
               numbers_per_lines = input_file.readlines()

           with open(even_file, 'w') as even_output_file, \
               open(odd_file, 'w') as odd_output_file:

               for line in numbers_per_lines:
                   cleaned_line = line.strip()