import pandas

data = pandas.read_csv('weather_data.csv')
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(round(average, 2))

print(round(data.temp.mean(), 2))

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

monday_temp = monday.temp[0]
print(monday_temp)

monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

data_dict = {
    'students': ['Leandro', 'Rafael', 'Jatna'],
    'scores': [76, 56, 65],
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv('new_file.csv')
