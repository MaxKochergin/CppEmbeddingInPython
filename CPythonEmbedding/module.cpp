#include <Windows.h>
#include <cmath>
#include <Python.h>//для CPython

//Реализация кода на C++
const double e = 2.7182818284590452353602874713527;

double sinh_impl(double x) {
    return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
}

double cosh_impl(double x) {
    return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x));
}

double tanh_impl(double x) {
    return sinh_impl(x) / cosh_impl(x);
}

// Обёрточная функция, преобразующая результат к PyObject
PyObject* tanh_implPy(PyObject* /* unused module reference */, PyObject* o) {
    double x = PyFloat_AsDouble(o);
    double tanh_x = tanh_impl(x);
    return PyFloat_FromDouble(tanh_x);
}

/*3. Добавили структуру, определяющую способ представления функции tanh_impl C++ для Python:*/
static PyMethodDef CPythonEmbedding_methods[] = {
    // The first property is the name exposed to Python, fast_tanh
    // The second is the C++ function with the implementation
    // METH_O means it takes a single PyObject argument
    { "fast_tanh", (PyCFunction)tanh_implPy, METH_O, nullptr },

    // Terminate the array with an object containing nulls.
    { nullptr, nullptr, 0, nullptr }
};
/*4 Добавим структуру, которая определит модуль так, как мы хотим ссылаться на него в коде Python, например, в from...import.
В приведенном ниже примере имя модуля "CPythonEmbedding" означает, что мы можем использовать from CPythonEmbedding import fast_tanh в Python,
так как fast_tanh определено в CPythonEmbedding_methods. Внутренние для проекта C++ имена файлов, такие как module.cpp, являются несущественными.
*/
static PyModuleDef CPythonEmbedding_module = {
    PyModuleDef_HEAD_INIT,
    "CPythonEmbedding",                        // Module name to use with Python import statements
    "Provides some functions, but faster",  // Module description
    0,
    CPythonEmbedding_methods                   // Structure that defines the methods of the module
};
/*5. Добавим метод, вызываемый Python при загрузке модуля. Он должен иметь имя PyInit_<module-name>,
где <module-name> точно соответствует значению свойства Общие>Целевое имя проекта C++.
То есть оно должно соответствовать имени файла с расширением .pyd, созданного проектом.*/
PyMODINIT_FUNC PyInit_CPythonEmbedding()
{
    return PyModule_Create(&CPythonEmbedding_module);
}