def get_most_frequent_word(text):
    counter_words= {}
    for i in text.split():
        counter_words[i]=counter_words.get(i,0)+1
    return max(counter_words,key=counter_words.get)
print(get_most_frequent_word("hello this is a string with words and spaces and big big woooooooooord and and and"))