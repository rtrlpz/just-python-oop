import pandas

data = pandas.read_csv('CensusSquirrel.csv')
# print(data)

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Red'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'count': [gray_squirrels_count, red_squirrels_count, cinnamon_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('squirrels_color_count.csv')