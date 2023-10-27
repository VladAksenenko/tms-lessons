def remove_vowels(lst):
    vowels_lst=["a","e","i","o","u"]
    vowels_no=list(filter(lambda letter : letter not in vowels_lst,lst))
    return vowels_no
string = list(input().split())
print(remove_vowels(string))