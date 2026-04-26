def find_highest_gwa(file_name):
    name_with_highest_gwa = ''
    highest_gwa = float('inf')

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()

                name, gwa = line.split(' - ')
                name = name.strip().title()
                gwa = float(gwa.strip())

                if gwa < highest_gwa:
                    highest_gwa = gwa
                    name_with_highest_gwa = name

            print(f'Student with the highest GWA: {name_with_highest_gwa} - {highest_gwa}')
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Invalid file Format')





