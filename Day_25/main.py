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

# data = pandas.read_csv("../Day_25/weather.csv")
# print(data['MinTemp'])
# data_json = data.to_json("../Day_25/weather.json")

# average_temp = data["MinTemp"].mean()
# print(round(average_temp, 2))
# print(data[data["RainTomorrow"] == "Yes"])

data = pandas.read_csv("../Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_color = len(data[data["Primary Fur Color"] == "Black"])

fur_color_count = {
    "Primary Fur Color": [" Gray", "Cinnamon", "Black"],
    "Number of Squarel": [gray_fur_color, cinnamon_fur_color, black_fur_color]
}

pandas.DataFrame(fur_color_count).to_csv("../Day_25/fur_color_count.csv")

print(fur_color_count)