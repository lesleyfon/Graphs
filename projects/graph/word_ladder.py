# Given two words (begin_word and end_word), and a dictionary's word list,
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

import string
from util import Stack, Queue  # These may come in handy

letters = []
for letter in string.ascii_lowercase:
    letters.append(letter)


f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    neighbors = set()

    string_word = word.split()

    for i in range(len(string_word)):
        for letter in letters:
            new_word = list(string_word)
            new_word[i] = letter

            new_word_string = "".join(new_word)
            if new_word_string in word_set and new_word_string != word:
                neighbors.append(new_word_string)


def find_word_path(begin_word, end_word):
    q = Queue
    visited = set()
    q.enqueue([begin_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word not in visited:

            if current_word == end_word:
                return current_path

            visited.add(current_word)

            for neighbors in get_neighbors(current_word):
                new_path = list(current_path)
                new_path.append(neighbors)

                q.enqueue(new_path)
