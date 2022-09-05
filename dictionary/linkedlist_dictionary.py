from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

    def get_value(self):
        return self.word_frequency

    def get_word(self):
        return self.word_frequency.word

    def get_frequency(self):
        return self.word_frequency.frequency

    def get_next(self):
        return self.next

    def set_value(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency

    def set_next(self, next):
        self.next = next


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------
# python3 dictionary_file_based.py linkedlist sampleDataToy.txt testToy.in testToy.out

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None
        self.length = 0


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        for words in words_frequencies:
            new_node = ListNode(words)

            if not self.head:
                self.head = new_node
            else:
                new_node.set_next(self.head)
                self.head = new_node

            self.length += 1

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        cur_node = self.head
        frequency = 0
        while cur_node:
            if cur_node.word_frequency.word == word:
                frequency = cur_node.word_frequency.frequency
            cur_node = cur_node.get_next()
        return frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        cur_node = self.head
        prev_node = None

        # Check if the current head is the value
        if cur_node.word_frequency == word_frequency:
            return False

        prev_node = cur_node
        cur_node = cur_node.get_next()

        # iterate through the list to find the matching word in node
        while cur_node:
            if cur_node.word_frequency == word_frequency:
                return False
            prev_node = cur_node
            cur_node = cur_node.get_next()

        new_node = ListNode(word_frequency)
        new_node = ListNode(word_frequency)
        if not self.head:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        if self.length == 0:
            return False

        cur_node = self.head
        prev_node = None

        # Check if the current head is the value
        if cur_node.word_frequency.word == word:
            self.head = cur_node.get_next()
            self.length-=1
            return True

        prev_node = cur_node
        cur_node = cur_node.get_next()

        # iterate through the list to find the matching word in node
        while cur_node:
            if cur_node.word_frequency.word == word:
                prev_node.set_next(cur_node.get_next())
                cur_node = None
                self.length-=1
                return True
            prev_node = cur_node
            cur_node = cur_node.get_next()

        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        res = []
        cur_node = self.head
        while cur_node:
            if cur_node.word_frequency.word.startswith(word):
                res.append(cur_node.word_frequency)
            cur_node = cur_node.get_next()
        res.sort(key=lambda x: x.frequency, reverse=True)
        return res[:3]





