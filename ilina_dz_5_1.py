#задание 1
def odd_num_to_n_gen(n):
	for odd_num in range(1, n, 2):
		yield odd_num

