import csv

file_name = 'calles_de_medellin_con_acoso.csv'

with open(file_name, newline='\n') as ar:
    data = csv.reader(ar,delimiter=';')

    streets = list(data)

print(streets)