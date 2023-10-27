from functools import reduce
def my_join(sequence: str, sep: str):
    return reduce(lambda w, x: w + sep + x, sequence.split())
string = input()
separator = input()
print(my_join(string, separator))