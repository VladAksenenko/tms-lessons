def generate_squares(*args):
    lst=[]
    for i in args :
        i=i**2
        lst.append(i)
    return lst
print(generate_squares(1,2,3))


def generate_squares(*args):
    lst=[i**2 for i in args]
    return lst
print(generate_squares(1,2,3))