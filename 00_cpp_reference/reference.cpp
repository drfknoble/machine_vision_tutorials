#include <algorithm>
#include <boost/asio.hpp>
#include <iostream>

int main(int argc, char* argv)
{

    // Single line comment

    /*
        Multiple line comment
    */

   int i = 0;
   float f = 0.0;
   bool A = false;
   bool B = false;
   bool C = false;
   bool D = false;
   int op1 = 1;
   int op2 = 2;
   double res = 0.0;
   bool test = false;

    // Operators (strongest to weakest)
    
    test = A && ( A && B ); // Brackets have strongest binding

    res = std::max(op1, op2); // Function

    res = std::pow(op1, op2); // Exponentation

    res = -op1; // Negation operator
    B = ! A; // Not operator

    res = op1 * op2; // Multiplication operator
    res = op1 / op2; // Division operator
    res = op1 % op2; // Modulo operator

    res = op1 + op2; // Addition operator
    res = op1 - op2; // Subtraction operator

    test = op1 < op2; // Less than operator
    test = op1 > op2; // Greater than operator
    test = op1 <= op2; // Less than or equal to operator
    test = op1 >= op2; // Greater than or equal to

    test = op1 == op2; // Equality operator

    C = A && B; // AND operator

    C = A != B; // XOR operator

    C = A || B; // OR operator
       
    // IF statement

    if (A == B)
    { // IF statement
        D = true;
    }

    if (A == B)
    { // IF-ELSE statement
        D = true;
    }
    else
    {
        D = false;
    }

    if (A == B)
    { // IF-ELSE IF statement
        D = true;
    }
    else if (A == C)
    {
        D = false;
    }

    // FOR statement

    f = 0.0;

    for( int i = 0; i < 5; i++)
    {
        f = f + i;
    }

    f = 0.0;

    for( int i = 0; i < 5; i++)
    {
        f = f + i;

        if (f > 3)
        {
            break;
        }
    }

    // WHILE statement

    i = 0;
    f = 0.0;

    while (f < 5)
    {
        i = i + 1;
        f = f + i;
    }

    i = 0;
    f = 0.0;

    while (f < 5)
    {
        i = i + 1;
        f = f + i;

        if (f > 3)
        {
            break;
        }
    }

    // Timing

    boost::asio::io_context io;

    boost::asio::steady_timer t(io, boost::asio::chrono::seconds(5));

    t.wait();
   
    return 0;
}
