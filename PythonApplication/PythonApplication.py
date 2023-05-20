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
    #test(lambda d: [fast_tanh(x) for x in d], 'Evaluation of tanh 500 000 times (CPython C++ extension)')
    #Pybind
    #pbObj = MathCalc()
    #test(lambda d: [pbObj.tanh_impl(x) for x in d], 'Evaluation of tanh 500 000 times] (PyBind11 C++ extension)')

    import os
    os.system("pause")

    #component test
    
    from PybindEmbedding import Component
    import PybindEmbedding as PE

    component1 = Component()
    component2 = Component()
    message1 = PE.Message(1.0,1)
    print(id(component2), ' : ', id(component2.outputDouble),' - ', component2.outputDouble)
    #component1.SendMessage(message1,component2)
    #component2.GetVoidPointer()
    #component1.SendMessagePy(message1,component2.GetVoidPointer())
    #component1.SendMessagePy(message1,PE.TransformPyObjectToVoid(component2))
    #component1.SendMessagePy(message1,component2.CreateCapsule())
    #a = component2.CreateCapsule()
    service = PE.Service()
    service.TestPointer(component2.pSelf)#,component2.pyPointer, component2.pyPointer)
    service.TestPointerPy(component2)
    component1.SendMessage(message1,service.VoidToComponent(component2.pSelf))
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print(id(component2), ' : ', id(component2.outputDouble),' - ', component2.outputDouble)

    #import ctypes
    #ctypes.byref() 

    os.system("pause")
