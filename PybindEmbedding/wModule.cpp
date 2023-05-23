#include <pybind11/pybind11.h>
#include "module.h"
#include "Component.h"
#include "wrapper.hpp"
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
    //testing send message function
    py::class_<Component>(m, "Component")
        .def(py::init<>())
        .def(py::init<std::string>())
        .def(py::init<std::string,int, int>())
        .def(py::init<std::string,double, double>())
        .def("SendMessage", &Component::SendMessagePy, py::call_guard<py::gil_scoped_release>())
        .def("AcceptMessage", &Component::AcceptMessage, py::call_guard<py::gil_scoped_release>())
        .def("CalculateFloat", &Component::CalculateFloat, py::call_guard<py::gil_scoped_release>())
        .def_readonly("outputDouble", &Component::outputDouble, byref)
        .def_readonly("name", &Component::name, byref)
        ;

    #ifdef VERSION_INFO
        m.attr("__version__") = VERSION_INFO;
    #else
        m.attr("__version__") = "dev";
    #endif
}
