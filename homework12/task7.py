import re


def generate_words(string: str) -> any:
    for word in re.findall(r'[а-яА-Яa-zA-Z]+', string):
        yield word


text = 'Мама. Мыла? Раму!'
for i in generate_words(text):
    print(i)

assert ["меня", "зовут", "Влад"] == [i for i in generate_words("меня зовут Влад")]
