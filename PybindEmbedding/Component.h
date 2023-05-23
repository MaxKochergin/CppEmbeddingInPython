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
    MessageC(void* data_in, messageType dataType_in)
    {
        data = data_in;
        dataType = dataType_in;
    }
    //MessageC(float dataIn, int dataTypeInInt)
    //{
    //    MessageC(dataIn, (messageType)dataTypeInInt);
    //}
    MessageC()
    {
        data = nullptr;
        dataType = noneType;
    }

};

class Component
{
public:
    std::string name;
    //input types - who knows what will come?
    int inputInt;
    double inputDouble;
    //output types - depends on input type
    int outputInt;
    double outputDouble;

    Component()
    {
        inputInt = 0; inputDouble = 0; outputInt = 1; outputDouble = 1;
        name = "-";
    }
    Component(std::string name_in, int input_in, int output_in)
    {
        inputInt = input_in; inputDouble = 0; outputInt = output_in; outputDouble = 1;
        name = name_in;
    }
    Component(std::string name_in, double input_in, double output_in)
    {
        inputInt = 0; inputDouble = input_in; outputInt = 0; outputDouble = output_in;
        name = name_in;
    }
    Component(std::string name_in)
    {
        inputInt = 0; inputDouble = 0; outputInt = 0; outputDouble = 0;
        name = name_in;
    }
    //Component(std::string name_in)
    //{
    //    inputInt = 0; inputDouble = 0; outputInt = 0; outputDouble = 0;
    //    name = name_in;
    //}

    //sending any data into next component in the circuit
    void SendMessage(Component* nextComponent, messageType mType)
    {
        MessageC* messageI = new MessageC(&this->outputInt, mType);
        MessageC* messageD = new MessageC(&this->outputDouble, mType);
        switch (mType)
        {

        case integerType:

            nextComponent->AcceptMessage(messageI);
            break;
        case floatType:

            nextComponent->AcceptMessage(messageD);
            break;
        }
        delete messageD;
        delete messageI;
    }
    void SendMessagePy(Component* nextComponent, int mType)
    {
        SendMessage(nextComponent, (messageType)mType);
    }
    //void SendMessagePy(MessageC message, PyObject* nextComponentCaps)
    //{
    //    void* p = PyCapsule_GetPointer(nextComponentCaps, NULL);
    //    Component* p1 = (Component*)p;
    //    p1->AcceptMessage(message);
    //}
    //processing received any data from previous component in the curcuit
    void AcceptMessage(MessageC *message)
    {
        if (message->data == nullptr)
            throw std::exception("Accepted data is empty");
        switch (message->dataType)
        {
        case floatType:
            inputDouble = *(double*)message->data;
            CalculateFloat();
            break;
        case integerType:
            inputInt = *(int*)message->data;
            CalculateInt();
            break;
        }

    }
    //processing float 
    void CalculateFloat()
    {
        outputDouble = inputDouble + outputDouble;
    }
    //processing int
    void CalculateInt()
    {
        outputInt = inputInt + outputInt;
    }
};
