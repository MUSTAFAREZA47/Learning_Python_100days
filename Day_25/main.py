# opening csv file from our basic open method in python
# with open("../Day_25/weather.csv") as data:
#     weather_datas = data.readlines()
#     for weather_data in weather_datas:
#         print(weather_data)


# importing csv file to handle csv data even more efficiently
# import csv
#
# with open("../Day_25/weather.csv") as data_file:
#     data = csv.reader(data_file)
#     min_Temp = []
#     for row in data:
#         if row[0] != "MinTemp":
#             min_Temp.append(float(row[0]))
#     print(min_Temp)


# using pandas library to read data more appealing
import pandas

data = pandas.read_csv("../Day_25/weather.csv")
print(data['MinTemp'])
