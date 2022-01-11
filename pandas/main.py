#how to read csv data files


# with open("weather_data.csv") as data_file :
#  data = data_file.readlines()
#  print(data)



#or


# import csv
# with open("weather_data.csv") as data_file :
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         #print(row[1])                  #temperatures are at index 1 (printing as integers)
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#             print(temperatures)


# references
# https://pandas.pydata.org/docs/getting_started/index.html#getting-started
# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats

import pandas

data = pandas.read_csv("weather_data.csv")



#to print the whole table        (dataframe)
print(data) 
# output
#    day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny



#to print coloumn               (series)                                    
print(data["temp"])
# output
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24    

                         

#to convert the type
data_dict = data.to_dict()
print(data_dict)
# output
# Name: temp, dtype: int64
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}



#to convert it into list and find average
temp_list = data["temp"].to_list()
print(len(temp_list))
average = sum(temp_list) / len(temp_list)
print(average)
# output
# [12, 14, 15, 14, 21, 22, 24]
# 17.428571428571427




## https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats

#mean method                             (without using average method)
print(data["temp"].mean())
# output
# 17.428571428571427

print(data["temp"].median())            #(to find middle temperature)       
#output
#15.0

print(data["temp"].max())               #(to find maximum temperature in that week)
#output
#24



#get data in coloums
print(data["condition"])
print(data.condition)                  
# output
# Name: condition, dtype: object
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny


#get data in rows  
print(data[data.day == "Monday"])
# output
# day  temp condition
# 0  Monday    12     Sunny


#which data in the row has the maximum temperature
print(data[data.temp == data.temp.max()])
# output
#       day  temp condition
# 6  Sunday    24     Sunny


#create a dataframe from scratch
data_dict = {
    "students": ["shreya", "shravya", "tina"],
    "scores" : [98, 72, 95]
}
data = pandas.DataFrame(data_dict)
#print(data)
data.to_csv("new_data_csv")
