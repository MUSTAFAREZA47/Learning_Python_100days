def add(*args):
    total = 0
    for n in args:
        total += n
    # print(total)


add(4, 5, 6, 5)


# *args will return tuple and **kwargs will return dictionary
def arg_func(a, *args, **kwargs):
    # print(a, args, kwargs)
    pass


arg_func(1, 7, 8, 4, x=4, y="abc")

