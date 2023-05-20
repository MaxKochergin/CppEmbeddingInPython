#pragma once
#include <string>
#include <Python.h>
//type of message data
enum messageType { noneType = -1, floatType, integerType, stringType };

//message - a way of components interaction
class MessageC
{
public:
    void* data;
    messageType dataType;
    MessageC(float dataIn, messageType dataTypeIn)
    {
        data = &dataIn;
        dataType = dataTypeIn;
    }
    MessageC(float dataIn, int dataTypeInInt)
    {
        MessageC(dataIn, (messageType)dataTypeInInt);
    }
    MessageC()
    {
        data = nullptr;
        dataType = noneType;
    }

};

void* FloatToVoid(double value)
{
    return (void*)&value;
}
double* VoidToFloat(void* data)
{
    return (double*)data;
}

void* TransformPyObjectToVoid(PyObject* pyob)
{
    return (void*)pyob;
}



class Component
{
public:
    //input types - who knows what will come?
    int inputInt;
    double inputDouble;
    std::string inputString;
    //output types - depends on imput type
    int outputInt;
    double outputDouble;
    std::string outputString;
    PyObject* pyPointer;
    void* pSelf;

    Component()
    {
        inputInt = 0; inputDouble = 0; outputInt = 0; outputDouble = 0;
        pSelf = this;
        pyPointer = PyLong_FromVoidPtr((void*)this);
        //pointer = PyCapsule_New(this, NULL, NULL);
    }

    PyObject* CreateCapsule(/*PyObject* self, PyObject* args*/)
    {
        PyObject* PyPointer;
        //PyPointer = PyCapsule_New((void*)this, NULL, NULL);
        PyPointer = PyLong_FromVoidPtr((void*)this);
        return PyPointer;
    }


    //void* GetVoidPointer()
    //{
    //    return PyCapsule_GetPointer(pointer,NULL);
    //}

    //sending any data into next component in the circuit
    void SendMessage(MessageC message, Component* nextComponent)
    {
        nextComponent->AcceptMessage(message);
    }
    void SendMessagePy(MessageC message, PyObject* nextComponentCaps)
    {
        void* p = PyCapsule_GetPointer(nextComponentCaps, NULL);
        Component* p1 = (Component*)p;
        p1->AcceptMessage(message);
    }
    //processing received any data from previous component in the curcuit
    void AcceptMessage(MessageC message)
    {
        switch (message.dataType)
        {
        case floatType:
            CalculateFloat();
            break;
        case integerType:
            CalculateInt();
            break;
        }

    }
    //processing float 
    void CalculateFloat()
    {
        outputDouble = inputInt + 1.0;
    }
    //processing int
    void CalculateInt()
    {
        outputInt = inputInt + 1.0;
    }
};
static class Service
{
public:
    Service(){}
    Component* VoidToComponent(void* pointer)
    {
        return (Component*)pointer;
    }
    void TestPointer(void* pField/*, PyObject* pyField, PyObject* pyOb*/)
    {
        void* p1 = pField;
        //void* p2 = (void*)pyField;
        //void* p3 = (void*)pyOb;
    }
    void TestPointerPy(py::object o)
    {
        void* p1 = o.;
        //void* p2 = (void*)pyField;
        //void* p3 = (void*)pyOb;
    }
};