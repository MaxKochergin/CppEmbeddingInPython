#include <pybind11/pybind11.h>
#include "module.h"

namespace py = pybind11;
constexpr auto byref = py::return_value_policy::reference_internal;
 
PYBIND11_MODULE(PybindEmbedding, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    py::class_<MathCalc>(m, "MathCalc")
        .def(py::init<>())
        .def(py::init<bool>())
        .def("tanh_impl", &MathCalc::tanh_impl, py::call_guard<py::gil_scoped_release>())
        .def("cosh_impl", &MathCalc::cosh_impl, py::call_guard<py::gil_scoped_release>())
        .def("sinh_impl", &MathCalc::sinh_impl, py::call_guard<py::gil_scoped_release>())
        .def_readonly("e", &MathCalc::e, byref)
        ;

    #ifdef VERSION_INFO
        m.attr("__version__") = VERSION_INFO;
    #else
        m.attr("__version__") = "dev";
    #endif
}