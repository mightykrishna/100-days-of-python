import pandas
data=pandas.read_csv("weather_data.csv")


#Create a dataframe from scratch

data_dict={
    "students":["Amyy","James","Angela"],
    "scores":[76,56,65]


}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")