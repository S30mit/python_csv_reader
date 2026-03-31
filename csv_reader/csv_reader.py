import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

print(read_csv('D:\\Practise\\csv_reader\\emp_details.csv'))
