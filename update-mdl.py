import csv
import io
import requests

r = requests.get('https://gitlab.cs.wwu.edu/tsikerm/assignment-files/raw/master/mdl.csv')

# print(r.text)

with open('mdl.csv', 'w') as mdlcsv:
    mdlcsv.write(r.text)
    # writer = csv.writer(mdlcsv)
    # writer.writerow(r.text)
# print(r.content)
with open('mdl.csv', 'r+') as f:
    lines = f.readlines()
    lines = lines[:-1]
    f.seek(0)
    f.truncate()
    for line in lines:
        f.write(line)
    # f.write(lines)

# for line in r.text:
#     print(line)

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