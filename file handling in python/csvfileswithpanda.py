import pandas

data=pandas.read_csv("weather_data.csv")
data_dict=data.to_dict()
#print(data_dict)

temp_list=data["temp"].to_list()
#print(len(temp_list))

#print(sum(data["temp"])/len(temp_list))
#print(data["temp"].mean())


#GET data in columns
#print(data["condition"])
#print(data.condition)

#GEt Data In ROw
print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])

monday=data[data.day=="Monday"]
print(monday.temp)