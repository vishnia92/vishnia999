#Задание 2(урок 2):  "05" часов "17" минут температура воздуха была "+05" градусов

weather_time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
for elem in weather_time.copy():
	if elem.isdigit():
		weather_time[index] = weather_time[index].zfill(2)
		weather_time.insert(index, '"')
		weather_time.insert(index+2, '"')
		index += 2
	elif elem.startswith(('+', '-')):
		weather_time[index] = f"{weather_time[index][0]}{weather_time[index][1:].zfill(2)}"
		weather_time.insert(index, '"')
		weather_time.insert(index+2,'"')
		index += 2
	index += 1
print(' '.join(weather_time).replace('"', '"').replace('"', '"'))



