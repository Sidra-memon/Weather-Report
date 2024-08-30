import csv
with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
data_dict= data.to_dict()
print(data_dict)
temp_list= data["temp"].to_list()
print(temp_list)
print(data["temp"].mean())
#get data in a rw
print(data[data.day =="Monday"])
#exact condition from monday colum
monday=(data[data.day =="Monday"])
print(monday.condition)



