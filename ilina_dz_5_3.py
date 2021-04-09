# 3 задание
tytors = [
	'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]
classes = [
	'9А', '7В', '9Б', '9В', '8Б', '10А'
]


def mir_zip():
	for index in range(len(tytors)):
		try:
			yield tytors[index], classes[index]
		except IndexError:
			yield tytors[index], None


generator = mir_zip()
print(*generator)
print(next(generator))
