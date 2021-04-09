src = [2, 8, 2, 7, 23, 99, 44, 44, 765, 1, 10, 7, 1, 11]
sss = set()
rep = set ()
for number in src:
	if number in sss:
		rep.discard(number)
	else:
		rep.add(number)
		sss.add(number)
print([number for number in src if number in rep])