import csv

# Reading from a CSV File
with open("matches.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)  # each row is a list
        if row[0]=='8': #8=match no #0=match no
            pom=row[10] # 10=pom
            print(pom)


#print(row[1]) # for team 1
#print(row[10]) # player of the match
#print((list(enumerate(row))):
#    break # to get row number and row