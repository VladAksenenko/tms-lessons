import re


class WordIterable:
    def __init__(self, string: str):
        self.string = re.findall(r"[а-яА-Я]+", string)
        self.count = -1

    def __iter__(self) -> any:
        return self

    def __next__(self) -> str:
        self.count += 1
        if len(self.string) == self.count:
            raise StopIteration()
        return self.string[self.count]


text = "мама. мыла? Раму!"
for i in WordIterable(text):
    print(i)

assert ["меня", "зовут", "Влад"] == [i for i in WordIterable("меня зовут Влад")]
assert ["мое", "увлечение", "это", "футбол"] == [i for i in WordIterable("мое увлечение - это футбол")]
