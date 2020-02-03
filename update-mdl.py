import csv

count = 1
first = 0
with open('ip.txt', 'r+') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('mdl.list', 'w+') as mdlfile:
        writer = csv.writer(mdlfile)
        for line in reader:
            count += 2
            rep = count
            if count > 128:
                rep = 3
            elif count > 100:
                rep = 127
            elif count < 20:
                rep = 1
            writer.writerow((line[0], 1, rep))
            