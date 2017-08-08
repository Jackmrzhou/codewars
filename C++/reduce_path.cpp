#include <iostream>
#include <vector>
#include <map>
class DirReduction
{
public:
    static std::vector<std::string> dirReduc(std::vector<std::string> &arr);
};
int main(void)
{
    std::vector<std::string> result;
    std::vector<std::string> d1 = {"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"};
    std::vector<std::string> d2 = {"NORTH","SOUTH","SOUTH","EAST","WEST","NORTH", "NORTH"};
    result = DirReduction::dirReduc(d2);
    for (auto it : result)
        std::cout << it;
    std::cout << std::endl;
    return 0;
}
std::vector<std::string> DirReduction::dirReduc(std::vector<std::string> &arr)
{
    std::map<std::string, int> direction;
    direction["NORTH"] = 1;
    direction["SOUTH"] = -1;
    direction["EAST"] = 2;
    direction["WEST"] = -2;
    std::vector<std::string> reduced_path{};
    std::string temp{};
    for (auto it : arr)
    {
        if (reduced_path.empty())
            reduced_path.push_back(it);
        else if (direction[it] == -direction[*(reduced_path.end()-1)])
            reduced_path.pop_back();
        else
            reduced_path.push_back(it);
    }
    return reduced_path;
}