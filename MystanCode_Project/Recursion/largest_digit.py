"""
File: largest_digit.py
Name:Mona Lai
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = str(n)
	if len(n) == 1:
		return n
	else:
		if n[0] > n[len(n) - 1]:
			new_n = n[0:len(n) - 1]
			return find_largest_digit(new_n)
		else:
			new_n = n[1:len(n)]
			return find_largest_digit(new_n)


if __name__ == '__main__':
	main()
