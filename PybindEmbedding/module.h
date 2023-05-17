#pragma once
#include <cmath>

//Реализация кода на C++
class MathCalc
{
    bool use;
public:
    //Конструктор без параметров
    MathCalc()
    {
        use = true;

    }

    //Конструктор с параметрами
    MathCalc(bool use_in)
    {
        use = use_in;
    }

    const float e = 2.7182818284590452353602874713527;

    //Методы для расчёта (для вызова из Python)
    float sinh_impl(float x) {
        return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
    }

    float cosh_impl(float x) {
        return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x));
    }

    float tanh_impl(float x) {
        return sinh_impl(x) / cosh_impl(x);
    }
};