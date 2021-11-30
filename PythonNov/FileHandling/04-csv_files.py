import csv

data = [
    ['firstname','lastname'],
    ['sachin','tendulkar'],
    ['rahul','dravid'],
    ['ms','dhoni'],
    ['virat','kohli']
]

with open('players.csv','w',newline='') as file:
    writer = csv.writer(file)
    # writer.writerows(data)
    for row in data:
        writer.writerow(row)

# with open('players.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


