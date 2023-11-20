def generate_words(string: str) -> any:
    for word in string.split():
        yield word


for i in generate_words('мама  мыла раму'):
    print(i)

assert ['2', '8', '44'] == [i for i in generate_words('0 1 4 9 16 25')]
assert not ['мама', '!', 'мыла44', 'раму', '?'] == [i for i in generate_words('мама!  мыла44 раму ?')]
