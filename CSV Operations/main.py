import csv

with open("C:\\Users\\moinm\\PycharmProjects\\Core_Python\\CSV Operations\\data.csv", 'r') as readObj:
    csv_reader = csv.DictReader(readObj)
    for line in csv_reader:
        print(line["Username"])
