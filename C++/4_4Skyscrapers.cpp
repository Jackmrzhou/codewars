#include <iostream>
#include <windows.h>
using namespace std;
bool success = false;
void check(int **m, int *clu)
{
    int c,min;
    for (int j = 0; j< 4; ++j)
    {
        c = 1,min = m[0][j];
        for (int a = 0; a < 4; ++a)
            if (m[a][j] > min)
            {
                min = m[a][j];
                c++;
            }
        if (c != clu[j] && clu[j] != 0) return;
    }
    for (int i = 0; i < 4; ++i)
    {
        c = 1, min = m[i][0];
        for (int a=0; a < 4; ++a)
            if (m[i][a] > min)
            {
                min = m[i][a];
                c++;
            }
        if (c != clu[15-i] && clu[15-i] != 0) return;
    }
    for (int j = 0; j < 4;++j)
    {
        c = 1, min = m[3][j];
        for (int a = 3; a>=0; --a)
            if (m[a][j] > min)
            {
                min = m[a][j];
                c++;
            }
        if (c != clu[11-j] && clu[11-j] != 0) return;
    }
    for (int i = 0; i < 4; ++i)
    {
        c = 1, min = m[i][3];
        for (int a= 3; a >= 0; --a)
            if (m[i][a] > min)
            {
                min = m[i][a];
                c++;
            }
        if (c != clu[4+i] && clu[4+i] != 0) return;
    }
    success = true;
}
void generate(int i,int j, int **m, int *clu)
{
    if (i == 4 && j == 0)
    {
        check(m,clu);
        return;
    }
    for (int k = 1; k <= 4; ++k)
    {
        if (success)
            return;
        bool flag = false;
        for (int a = 0; a < i; ++a)
            if (m[a][j] == k) flag = true;
        for (int a = 0; a<j; ++a)
            if (m[i][a] == k) flag = true;
        if (flag)
            continue; 
        m[i][j] = k;
        if (j==3)
            generate(i+1,0,m,clu);
        else
            generate(i,j+1,m,clu);  
    }
}

int** SolvePuzzle (int *clues) 
{
    int **matrix = new int*[4];
    for (int i = 0; i <4; ++i)
        matrix[i] = new int[4];
    success = false;
    for (int i = 1; i <= 4; ++i)
    {
        matrix[0][0] = i;
        generate(0,1,matrix,clues);
        if (success)
            break;
    }
    return matrix;
}

int main()
{
    int clues[16] = { 0, 0, 1, 2,   
                      0, 2, 0, 0,   
                      0, 3, 0, 0, 
                      0, 1, 0, 0 };
    auto res = SolvePuzzle(clues);
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
            cout << res[i][j] << ',';
        cout << endl;
    }
    return 0;
}