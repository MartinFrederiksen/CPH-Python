import csv

def print_file_content(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def write_list_to_file(output_file, *lst):
    with open(output_file, 'w') as outFile:
        for string in lst:
            outFile.write(string + '\n')


def read_csv(input_file):
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file)
        result = []
        for row in reader:
            result.append(row)
        return result