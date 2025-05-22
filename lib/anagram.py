class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        sorted_word = sorted(self.word)
        return [candidate for candidate in candidates if sorted(candidate) == sorted_word]

      
