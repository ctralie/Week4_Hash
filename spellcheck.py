from strwrapper import StrWrapper
from hashtable import *

class SpellChecker:
    """
    Given a list of words, identify what words are spelled correctly
    from a 'training' corpus of words.
    """
    def __init__(self, num_words, path="words.txt"):
        """
        For each word in the corpus related to the specified path, extract
        num_words and store them in a hashmap for quick access.
        """
        self.num_words = num_words
        fin = open(path, encoding="utf8")
        lines = fin.readlines()
        # A good thing to do is to make the number of buckets equal
        # to the number of expected objects, up to a constant
        self.words = HashTable(len(lines))
        for line in lines:
            # Convert string to StrWrapper to get hashcode
            s_word = StrWrapper(line.split()[0].strip().rstrip()) 
            self.words.add(s_word) # add word to hashmap based on hashcode
    
    def check(self, word):
        """
        Identify is a given word is spell correctly by identifying if it
        exists in our list of training words.
        
        Params
        ------
        word: a string; any word to check seplling
        
        Return
        ------
        res: true is the word exists in self.words, false otherwise
        """
        res = False
        s_word = StrWrapper(word.lower())
        if self.words.contains(s_word):
            res = True
        return res