class reversestring:
    def __init__(self,sentence):
        self.sentence = sentence
    def reverse_words(self):
        words=self.__sentence.split()
        reversedwords=word [::-1]
        return ' '.join(reversedwords)
    def __str__(self):
        return self.reversedwords()
text=reversestring("this is phyton")
print(text.reverse_words())

    