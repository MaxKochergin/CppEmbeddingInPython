#based on:
#https://learn.microsoft.com/ru-ru/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2019
# additional for Pybind:
# https://www.matecdev.com/posts/cpp-call-from-python.html
# and
# https://smyt.ru/blog/sozdaem-s-python-rasshireniya-s-pomshyu-pybind11/

from random import random
from time import perf_counter
from CPythonEmbedding import fast_tanh
from PybindEmbedding import MathCalc

COUNT = 500000  # Change this value depending on the speed of your computer
DATA = [(random() - 0.5) * 3 for _ in range(COUNT)]

#Native Python Implementation
e = 2.7182818284590452353602874713527

def sinh(x):
    return (1 - (e ** (-2 * x))) / (2 * (e ** -x))

def cosh(x):
    return (1 + (e ** (-2 * x))) / (2 * (e ** -x))

def tanh(x):
    tanh_x = sinh(x) / cosh(x)
    return tanh_x

# Testing
def test(fn, name):
    start = perf_counter()
    result = fn(DATA)
    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    for d in result:
        assert -1 <= d <= 1, " incorrect values"

# Main
if __name__ == "__main__":
    print('Running benchmarks with COUNT = {}'.format(COUNT))
    #Native
    test(lambda d: [tanh(x) for x in d], 'Evaluation of tanh 500 000 times (Python native implementation)')
    #CPython
    test(lambda d: [fast_tanh(x) for x in d], 'Evaluation of tanh 500 000 times (CPython C++ extension)')
    #Pybind
    pbObj = MathCalc()
    test(lambda d: [pbObj.tanh_impl(x) for x in d], 'Evaluation of tanh 500 000 times] (PyBind11 C++ extension)')

    import os
    os.system("pause")