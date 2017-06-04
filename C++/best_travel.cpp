#include <iostream>
#include <vector>
class BestTravel
{
public:
    static int chooseBestSum(int t, int k, std::vector<int>& ls);
};
int main(void)
{
    std::vector<int> ts = {50, 55, 56, 57, 58};
    int n = BestTravel::chooseBestSum(163, 1, ts);
    std::cout << n << std::endl;
    return 0;
}
int BestTravel::chooseBestSum(int t, int k, std::vector<int>& ls)
{
    if(k > int(ls.size()))
        return -1;
    std::vector<int> stack{};
    int temp{},count{},result{};
    for (int i = 0; i != k;++i)
    {
        stack.push_back(i);
        result += ls[i];
    }
    result = result <= t ? result : 0;
    while(stack[0] != (int)ls.size()-k)
    {
        int sum{};
        do{
            count += 1;
            temp = *(stack.end() - 1);
            stack.pop_back();
        }while(temp >= (int)ls.size()-count);
        int i(1);
        while(count > 0)
        {
            stack.push_back(temp + i);
            ++i;
            count--;
        }
        for (auto e:stack)
            sum += ls[e];
        if(sum <= t && sum > result){
            result = sum;
        }
    }
    return result == 0 ? -1 : result;
}