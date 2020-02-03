import csv
import re
# import io
# import requests

# r = requests.get('https://gitlab.cs.wwu.edu/tsikerm/assignment-files/raw/master/mdl.csv')

# print(r.text)

# with open('mdl.csv', 'w') as mdlcsv:
#     mdlcsv.write(r.text)
    # writer = csv.writer(mdlcsv)
    # writer.writerow(r.text)
# print(r.content)
with open('mdl.csv', 'r+') as f:
    lines = f.readlines()
    lines = lines[:-1]
    # print(len(lines))
    # lines = list(set(lines))
    # print(len(lines))
    f.seek(0)
    f.truncate()
    for line in lines:
        # print(line)
        f.write(line)
    # f.write(lines)

# for line in r.text:
#     print(line)
counter = 1
counter2 = 1
with open('mdl.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open('mdl.list', 'w') as mdlfile:
        writer = csv.writer(mdlfile)
        for line in reader:
            # print(line)
            # print(len(line))
            if len(line) != 0:
                # print(line)
                rep = len(line[1])
                # ip = line[2]
                ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line[2] )
                # ip = "140.160." + str(counter2) + "." + str(counter)
                counter += 1
                if counter > 254:
                    counter = 1
                    counter2 += 1
                # print(line[2],"->",ip)
                num = ip[0]
                # print(num)

                # rep = urlLen // 127
                if rep < 1:
                    rep = 1
                elif rep > 127:
                    rep = 127
                else:
                    rep = rep // 5
                if rep < 1:
                    rep = 1
                writer.writerow((ip[0], 1, rep))