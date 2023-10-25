def generate_natural_cubes(n:int):
    lst=[]
    for i in range (n):
        i=i**3
        lst.append(i)
    return lst
print(generate_natural_cubes(12))


def generate_natural_cubes(n:int):
    lst =[i**3 for i in range(n)]
    return lst
print(generate_natural_cubes(12))