# Чтения
import _csv
from collections import defaultdict
#print(_csv.__file__)
capacity = []
cost = []
with open('test_csv.csv', 'r',encoding='utf-8') as fp:
    reader = _csv.reader(fp, delimiter=',', quotechar='"')
    for row in reader:
        print(row[0], " - ", row[1], " - ", row[2], " - ", row[3])
        row1= row[1]
        row2 = row[2]
        capacity.append(row1)
        cost.append(row2)
        #print(columns.append(row2))

#x = capacity.index("4400")
#cost[x]
#print(cost[x])
