import csv

# Writing to a CSV File
with open("CSV_File.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 45, "India"])



# Reading from a CSV File
with open("CSV_File.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # each row is a list



