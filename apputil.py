import numpy as np
from collections import defaultdict

class MarkovText:
    
    def __init__(self, corpus):
        self.corpus = corpus
        self.tokens = corpus.split()
        self.term_dict = None
    
    def get_term_dict(self):
        term_dict = defaultdict(list)
        
        for i in range(len(self.tokens) - 1):
            current_word = self.tokens[i]
            next_word = self.tokens[i + 1]
            term_dict[current_word].append(next_word)
        
        self.term_dict = dict(term_dict)
        return self.term_dict