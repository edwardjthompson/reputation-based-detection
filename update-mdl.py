import csv
# import io
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
        # print(line)
        f.write(line)
    # f.write(lines)

# for line in r.text:
#     print(line)

with open('mdl.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('mdl.list', 'w') as mdlfile:
        writer = csv.writer(mdlfile)
        for line in reader:
            print(line)
            # print(len(line))
            if len(line) != 0:
                # print(line)
                urlLen = len(line[1])
                rep = urlLen // 127
                if rep < 1:
                    rep = 1
                elif rep > 127:
                    rep = 127
                writer.writerow((line[2], 1, rep))