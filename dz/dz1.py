def func(a, *args):
    for i in range(a):
        d = []
        d.append(args[i])
    return d


print(func(2, 3, 5))



