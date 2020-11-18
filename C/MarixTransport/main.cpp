#include<iostream>
using namespace std;
template<class T>
void swap(T* a, T* b)
{
    T temp = a;
    a = *b;
    *b = temp;
    return;
}
template<class T>
void transpose(T& a, int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = i + 1;j<rows; j++)
        {
            swap(a[i][j], a[j][i]);
        }
    }
    return;
}
int main()
{
    int a[3][4] = { 1,2,3,4,5,6,7,8,7,9,11,12 };
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    transpose(a,4);
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3;j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
