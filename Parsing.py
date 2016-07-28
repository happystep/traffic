import csv

def parse(filename):
# filename = 'I-35 @ I-35 SB TO I 435 WB FF - First Trimester.csv'
    current = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            current.append(row)
        return current
        # thought process of returning the reader, and then making this a funciont,... loop thru it in main and then, save what is returned which are dictionaries in a list in main. then figu
        # out what to do with the data from there to make it a sturcutre that will be easily queried