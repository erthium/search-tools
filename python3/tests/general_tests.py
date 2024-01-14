import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, '../')
sys.path.append(SRC_DIR)

from distance import iterative_lev, similarity_percentage, word_in_word, simplyfy
from unittest import TestCase, main


class TestDistance(TestCase):
    def test_iterative_lev(self):
        self.assertEqual(iterative_lev("1234", "4321"), 4)
        self.assertEqual(iterative_lev("a", "1234"), 4)
        self.assertEqual(iterative_lev("foo", "baz"), 3)
        self.assertEqual(iterative_lev("asd", "asd"), 0)
        self.assertEqual(iterative_lev("123456789123456789", "912345678912345678"), 2)
    
    def test_similarity_percentage(self):
        self.assertEqual(similarity_percentage("asd", "asd"), 1)
        self.assertEqual(similarity_percentage("asd", "asdd"), 0.75)
        self.assertEqual(similarity_percentage("asd", "asddd"), 0.6)
        self.assertEqual(similarity_percentage("asd", "asdddd"), 0.5)
    
    def test_word_in_word(self):
        self.assertEqual(word_in_word("asd", "asd"), True)
        self.assertEqual(word_in_word("asd", "asdd"), True)
        self.assertEqual(word_in_word("asd", "asddd"), True)
        self.assertEqual(word_in_word("asd", "asdddd"), True)
    
    def test_simplyfy(self):
        self.assertEqual(simplyfy("Staré Město"), "stare mesto")
        self.assertEqual(simplyfy("ÇŞĞİüö"), "csgiuo")
        self.assertEqual(simplyfy("Iñtërnâtiônàlizâtiôn"), "internationalization")


if __name__ == '__main__':
    main()
