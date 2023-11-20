class WordIterable:
    def __init__(self, string: str):
        self.string = string.split()
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if len(self.string) == self.count:
            raise StopIteration()
        return self.string[self.count]


text = ('Всем привет меня зовут Влад')

for word in WordIterable(text):
    print(word)