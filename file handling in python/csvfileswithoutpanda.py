import csv

with open("weather_data.csv") as data_file:

    data=csv.reader(data_file)
    temp=[]
    for row in data:
        if row[1]!="temp":
            temp.append(row[1])
    print(temp)