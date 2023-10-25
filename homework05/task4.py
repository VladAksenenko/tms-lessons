def get_longest_word(str):
    words=str.split()
    long_word=""
    for i in words:
        if len(i)>len(long_word):
            long_word=i
    return long_word
print(get_longest_word("hello this is a string with words and spaces and big big woooooooooord"))