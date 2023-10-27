def map_to_tuples(lst):
    return list(map(lambda x: (x.upper(), x.lower()), lst))

string = list(input().split())
print(map_to_tuples(string))