"""
File: boggle.py
Name:Mona
----------------------------------------

"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
d_list = []


def main():
	"""
	It is a boggle game.
	"""
	all_word = []
	row1 = input('1 row of letters:')
	row1_lst = row1.split()
	for i in range(len(row1_lst)):
		if len(row1_lst[i]) >= 2:
			print('Illegal input')
		if len(row1_lst) > 4 or len(row1_lst) < 4:
			print('Illegal input')
			break
	all_word.append(row1_lst)
	row2 = input('2 row of letters:')
	row2_lst = row2.split()
	for i in range(len(row2_lst)):
		if len(row2_lst[i]) >= 2:
			print('Illegal input')
		if len(row2_lst) > 4 or len(row2_lst) < 4:
			print('Illegal input')
	all_word.append(row2_lst)
	row3 = input('3 row of letters:')
	row3_lst = row3.split()
	for i in range(len(row3_lst)):
		if len(row3_lst[i]) >= 2:
			print('Illegal input')
		if len(row3_lst) > 4 or len(row3_lst) < 4:
			print('Illegal input')
	all_word.append(row3_lst)
	row4 = input('4 row of letters:')
	row4_lst = row4.split()
	for i in range(len(row4_lst)):
		if len(row4_lst[i]) >= 2:
			print('Illegal input')
		if len(row4_lst) > 4 or len(row4_lst) < 4:
			print('Illegal input')
	all_word.append(row4_lst)
	ans_list = []
	start = time.time()
	read_dictionary()
	find_boggle(all_word, ans_list)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			d_list.append(line.strip())


def find_boggle(all_word, ans_list):
	for y in range(len(all_word)):
		for x in range(len(all_word[y])):
			letters = all_word[y][x]
			find_boggle_helper(all_word, ans_list, x, y, '', [])


def find_boggle_helper(all_word, ans_list, cur_x, cur_y, cur_str, cur_index):
	if len(cur_str) >= 4:
		if cur_str in d_list:
			if cur_str not in ans_list:
				ans_list.append(cur_str)
				print('Found: ' + cur_str)
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			side_x = j+cur_x
			side_y = i+cur_y
			if 0 <= side_x < 4:
				if 0 <= side_y < 4:
					# Choose
					if (side_x, side_y) not in cur_index:
						cur_str += all_word[side_y][side_x]
						cur_index.append((side_x, side_y))

						# Explore
						if has_prefix(cur_str):
							find_boggle_helper(all_word, ans_list, side_x, side_y, cur_str, cur_index)

						# Un-choose
						cur_str = cur_str[0:len(cur_str)-1]
						cur_index.pop()


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
