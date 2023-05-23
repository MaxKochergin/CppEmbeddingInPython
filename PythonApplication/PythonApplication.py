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
from NativePythonCalc import *

COUNT = 500000  # Change this value depending on the speed of your computer
DATA = [(random() - 0.5) * 3 for _ in range(COUNT)]

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
    import os
    answer = input('Type 0 if you want to run Tanh calculator or type 1 if you want to run Component messaging.\n>>')
    match answer:
        #Tanh calculator
        case '0':
            print('Running benchmarks with COUNT = {}'.format(COUNT))
            #Native
            test(lambda d: [tanh(x) for x in d], 'Evaluation of tanh 500 000 times (Python native implementation)')
            #CPython
            test(lambda d: [fast_tanh(x) for x in d], 'Evaluation of tanh 500 000 times (CPython C++ extension)')
            #Pybind
            pbObj = MathCalc()
            test(lambda d: [pbObj.tanh_impl(x) for x in d], 'Evaluation of tanh 500 000 times] (PyBind11 C++ extension)')
            os.system("pause")
    
        #component test
        case '1':
            from PybindEmbedding import Component

            #Component 1 is sending data
            component1 = Component('Component 1',0.0,1.0)
            #Component 2 is receiving and calculating data
            component2 = Component('Component 2', 0.0,0.0)
 
            for i in range(4):
                #component 1 sends message1 to component2
                component1.SendMessage(component2,0)
                print(i,': ' , component1.name, ' at ', id(component1), 'sends message ', component1.outputDouble, ' to ', 
                      component2.name, ' at ', id(component2), '. Now output 2 is ', component2.outputDouble)

            os.system("pause")
        case _:
            print('Wrong choice. Restart and try again.')
