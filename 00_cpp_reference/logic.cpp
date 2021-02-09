#include <iostream>
#include <vector>

int main(int argc, char* argv)
{

    std::vector<bool> A{false, true};
    std::vector<bool> B{false, true};

    std::cout << "Bolean AND" << std::endl;

    for (auto &a : A)
    {
        for (auto &b : B)
        {
            bool c = a && b;

            std::cout << a << " AND " << b << " = " << c << std::endl;
        }
    }
    std::cout << std::endl;

    std::cout << "Bolean XOR" << std::endl;

    for (auto &a : A)
    {
        for (auto &b : B)
        {
            bool c = a != b;

            std::cout << a << " XOR " << b << " = " << c << std::endl;
        }
    }
    std::cout << std::endl;

    std::cout << "Bolean OR" << std::endl;

    for (auto &a : A)
    {
        for (auto &b : B)
        {
            bool c = a || b;

            std::cout << a << " OR " << b << " = " << c << std::endl;
        }
    }
    std::cout << std::endl;

    std::cout << "Bolean NOT" << std::endl;

    for (auto &a : A)
    {
        bool b = ! a;

        std::cout << "NOT" << a << " = " << b << std::endl;
        
    }

    return 0;
}