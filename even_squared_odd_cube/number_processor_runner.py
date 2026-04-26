from number_processor import NumberProcessor

def main():
    number_processor = NumberProcessor('integers.txt')
    number_processor.process_numbers('double.txt', 'triple.txt')