"""
File: anagram.py
Name:Mona Lai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic = []
ans_list = []


def main():
    """
    This program could help to find the all the anagram(s) which you input.
    """
    global ans_list
    start = time.time()
    ####################
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagram for:')
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
        print(str(len(ans_list)) + 'anagrams:' + str(ans_list))
        ans_list = []
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            words = line.strip()
            dic.append(words)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    find_anagrams_helper(s, [], '')


def find_anagrams_helper(s, cur_list, cur_str):
    if len(cur_str) == len(s):
        if cur_str in dic:
            if cur_str not in ans_list:
                ans_list.append(cur_str)
                print('Found: '+cur_str)
                print('Searching...')
    else:
        for i in range(len(s)):
            if i not in cur_list:
                # Choose
                cur_list.append(i)
                cur_str += s[i]
                # Explore
                find_anagrams_helper(s, cur_list, cur_str)
                # Un-choose
                cur_list.pop()
                cur_str = cur_str[ :-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    if sub_s.startswith(sub_s):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
