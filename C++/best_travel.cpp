#include <iostream>
#include <vector>
#include <algorithm>
class BestTravel
{
public:
    static int chooseBestSum(int t, int k, std::vector<int>& ls);
};
int main(void)
{
    std::vector<int> ts = {50, 55, 56, 57, 58};
    int n = BestTravel::chooseBestSum(163, 3, ts);
    std::cout << n << std::endl;
    return 0;
}
int BestTravel::chooseBestSum(int t, int k, std::vector<int>& ls)
{
    if (k > (int)ls.size())
        return -1;
    sort(ls.begin(), ls.end());
    int sum{},m{},temp{};
    while (temp <= t)
    {
        sum = temp;
        temp = 0;
        for (int i(0); i != k;++i)
            temp += ls[i+m];
        if (m < (int)ls.size()-k)
            ++m;
        else
            break;
    }
    return sum ;
}