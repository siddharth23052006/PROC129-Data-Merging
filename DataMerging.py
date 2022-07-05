import csv

dataset1 = []
dataset2 = []

with open("Bright_Stars.csv") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    dataset1.append(row)

with open("Brown_Dwarfs_Masses_Radii.csv") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    dataset2.append(row)

header1 = dataset1[0]
star_data1 = dataset1[1:]

header2 = dataset2[0]
star_data2 = dataset2[1:]

headers = header1 + header2
star_data = []

for index, data_row in enumerate(star_data1):
  star_data.append(star_data1[index] + star_data2[index])

with open("Merged_Stars.csv", "w") as merge:
  csvwriter = csv.writer(merge)
  csvwriter.writerow(headers)
  csvwriter.writerows(star_data)