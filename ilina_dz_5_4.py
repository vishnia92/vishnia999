#4 задание
src = [2, 8, 2, 7, 23, 99, 44, 44, 765, 1, 10, 7, 1, 11]

result = []
for index in range(1, len(src)):
	if src[index-1] < src[index]:
		result.append(src[index])
print(result)