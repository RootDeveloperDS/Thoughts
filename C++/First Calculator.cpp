#include<iostream>
using namespace std;

int main()
{
    int oper1,oper2;
    char sign;
    cout << "choose the operation you want to perform from below\n( +,-,*,/ ) " << endl;
    cin >> sign;
    cout <<"Enter your first number : \n";
    cin >> oper1;
    cout <<"Enter your second number : \n";
    cin >> oper2;
    
    if (sign == '+')
    {
        cout <<oper1<<sign<<oper2<<"="<<oper1+oper2<<endl;
    }
    else if (sign == '-')
    {
        cout <<oper1<<sign<<oper2<<"="<<oper1-oper2<<endl;
    }
    else if (sign == '*')
    {
        cout <<oper1<<sign<<oper2<<"="<<oper1*oper2<<endl;
    }
    else if (sign == '/')
    {
        cout <<oper1<<sign<<oper2<<"="<<oper1/oper2<<endl;
    }

    return 0;
}