def remove_vowels(lst):
    return list(filter(lambda c: c.lower() not in ['a', 'e', 'i', 'o', 'u', 'y'], lst))
string = list(input().split())
print(remove_vowels(string))