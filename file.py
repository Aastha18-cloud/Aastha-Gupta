# Write code below 💖
import csv
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
  file=open("packing_list.csv","r",newline='')
  for lines in data:
    print(lines)
except:
  print(" FileNotFoundError.")
  print("Packing list file not found. Creating a new one.")
  file2=open("packing_list.csv","w",newline='')
  csv_writer=csv.writer()
  csv.writerows(data)