import csv

with open('mdl.list', newline='') as csvfile:
    sum = 0
    count = 0
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in reader:
        count += 1
        sum += int(line[2])

    print(sum / count)