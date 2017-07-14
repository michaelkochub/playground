import timeit

no_resize = """
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
b = {'c': 3, 'd': 4, 'a': 1, 'b': 2}
"""

resize = """
c = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
"""

print("Dictionaries:\n-----------")
print("No resizing: {}".format(timeit.Timer(stmt=no_resize).timeit(100000)))
print("Resizing: {}".format(timeit.Timer(stmt=resize).timeit(100000)))

smaller = """
a = [0, 1, 2].extend([3, 4, 5])
"""

bigger = """
c = [0, 1, 2].extend([3, 4, 5, 6, 7, 8, 9, 10])
"""

print("\nLists:\n-----------")
print("Extend Small: {}".format(timeit.Timer(stmt=smaller).timeit(100000)))
print("Extend Big: {}".format(timeit.Timer(stmt=bigger).timeit(100000)))
