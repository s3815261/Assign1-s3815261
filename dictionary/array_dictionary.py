from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

# python3 dictionary_file_based.py array sampleDataToy.txt testToy.in testToy.out


class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.dict = []
        pass

    def sort_dictonary(self):
        """
        sort the dictonary by the words in alphabetical order
        @param dict: list of tuples (word, frequency)
        @return: dictonary: in alphabetical order
        """
        self.dict.sort(key = lambda words: words[0])

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for words in words_frequencies:
            # Convert WordFrequency into Tuple that can be added to list
            word = (words.word, words.frequency)
            # Append word tuple to list
            self.dict.append(word)
        ArrayDictionary.sort_dictonary(self)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # Search our list by a key: WORD --> for example 'cut'
        # Iterate though list
        # if dict[i] matches with the key word
        # Return index!
        # Assume that all words are UNIQUE && Lowercase!!!
        word_frequency = 0
        for words in self.dict:
            if words[0] == word:
                word_frequency = words[1]
        return word_frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # Check if the word exists in the dictionary
        for words in self.dict:
            if (words[0] == word_frequency.word) & (words[1] == word_frequency.frequency):
                return False
        word = word_frequency.word, word_frequency.frequency
        self.dict.append(word)
        # Ensure that the order is kept...
        # Can use BISECT method but for now... increases complexity...
        # A.K.A I'm dumb so this will increase the time complexity
        ArrayDictionary.sort_dictonary(self)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list
        # Assuming that list is UNIQUE && First word to delete!
        # TO BE IMPLEMENTED
        flag = False
        for words in self.dict:
            if words[0] == word:
                self.dict.remove(words)
                flag = True
        return flag

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        res = []
        for words in self.dict:
            if words[0].startswith(prefix_word):
                word = WordFrequency(words[0], words[1])
                res.append(word)
        res.sort(key=lambda x: x.frequency, reverse=True)
        return res[:3]
