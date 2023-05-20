#include <pybind11/pybind11.h>
#include "module.h"
#include "Component.h"
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
    //testin send message function
    py::class_<Component>(m, "Component")
        .def(py::init<>())
        .def("SendMessage", &Component::SendMessage, py::call_guard<py::gil_scoped_release>())
        .def("SendMessage", &Component::SendMessagePy, py::call_guard<py::gil_scoped_release>())
        .def("AcceptMessage", &Component::AcceptMessage, py::call_guard<py::gil_scoped_release>())
        .def("CalculateFloat", &Component::CalculateFloat, py::call_guard<py::gil_scoped_release>())
        .def("CreateCapsule", &Component::CreateCapsule, py::call_guard<py::gil_scoped_release>())
        //.def("GetVoidPointer", &Component::GetVoidPointer, py::call_guard<py::gil_scoped_release>())
        .def_readonly("outputDouble", &Component::outputDouble, byref)
        .def_readonly("pyPointer", &Component::pyPointer, byref)
        .def_readonly("pSelf", &Component::pSelf, byref)
        ;

    py::class_<Service>(m, "Service")
        .def(py::init<>())
        .def("VoidToComponent", &Service::VoidToComponent, py::call_guard<py::gil_scoped_release>())
        .def("TestPointer", &Service::TestPointer, py::call_guard<py::gil_scoped_release>())
        .def("TestPointerPy", &Service::TestPointerPy, py::call_guard<py::gil_scoped_release>())
        ;

    //message
    py::class_<MessageC>(m, "Message")
        .def(py::init<double, int>())
        .def(py::init<>())
        ;
    m.def("TransformPyObjectToVoid", &TransformPyObjectToVoid, py::call_guard<py::gil_scoped_release>());
    #ifdef VERSION_INFO
        m.attr("__version__") = VERSION_INFO;
    #else
        m.attr("__version__") = "dev";
    #endif
}
