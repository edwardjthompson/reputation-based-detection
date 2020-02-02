import csv

with open('mdl.list', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in reader:
        for line2 in reader:
            # print (line, line2)
            # l1 = line.split(",")
            # l2 = line2.split(",")
            # print(line[0], line2[0])
            if line[0] == line2[0]:
                print(line)
        