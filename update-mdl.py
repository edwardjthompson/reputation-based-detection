import csv

with open('mdl.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('mdl.list', 'w') as mdlfile:
        writer = csv.writer(mdlfile)
        for line in reader:
            # print(line)
            # if len(line) > 0:
            # print(line[2])
            # print(line[1])
            # print(len(line[1]), "\n")
            # <ip>,<category>,<reputation score>
            # print(line[2], 1, len(line[1]))
            writer.writerow((line[2], 1, len(line[1])))