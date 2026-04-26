from number_processor import NumberProcessor

def main():
    new_number = NumberProcessor('integers.txt')
    new_number.process_numbers('double.txt', 'triple.txt')

if __name__ == '__main__':
    main()