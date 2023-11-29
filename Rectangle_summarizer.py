import csv
from statistics import mean
with open("DATA475_lab_rectangles_data.csv") as f:
    next(f)
# #print(f.read())
# for row in f:
#     print(row.split(','))
# f.close()
    reader = csv.reader(f)
    areas = []
    for row in reader:
        area= float(row[1]) * float(row[2])
        areas.append(area)
    # print(areas)
    # print('Total',len(areas))
    # print('Max',max(areas))

summary = {
    'Total Count': len(areas),
    'Sum Area': sum(areas),
    'Max Area': max(areas),
    'Min Area': min(areas),
    'Ave Area': mean(areas),
}
for key,value in summary.items():
    print(f'{key}:{value}')

with open('summary.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())