#include <iostream>
#include <array>
#include <string>
#include <map>
class Mix
{
public:
  static std::string mix(const std::string &s1, const std::string &s2);
};
class count_char
{
    public:
        count_char(int s1,int s2): count[0] = s1, count[1]=s2{}
        auto compare() -> std::array<int, 2>;
        std::array<int, 2> count;
};
int main(void)
{
    std::string s1 = "my&friend&Paul has heavy hats! &";
    std::string s2 = "my friend John has many many friends &";
    std::string result = Mix::mix(s1, s2);
    std::cout << result << std::endl;
    return 0;
}
auto count_char::compare() -> std::array<int, 2>
{
    std::array<int, 2> temp{};
    if (count[0] > count[1])
    {
        temp[0] = 1;
        temp[1] = count[0];
    }
    else if (count[0] < count[1])
    {
        temp[0] = 2;
        temp[1] = count[1];
    }
    else{
        temp[0] = 3;
        temp[1] = count[1];
    }
    return temp;
}
std::string Mix::mix(const std::string &s1, const std::string &s2)
{
    std::string result{};
    std::map<char, count_char> record_map{};
    for (const auto &ch : s1)
    {
        if (record_map.find(ch) == record_map.end() &&
            ch >='a' && ch <= 'z')
        {
            record_map.insert(make_pair(ch, count_char(1, 0)));
        }
        else 
        {
            (record_map[ch].count)[0] += 1;
        }
    }
    for (const auto &ch : s2)
    {
        if (record_map.find(ch) == record_map.end() &&
            ch >='a' && ch <= 'z')
        {
            record_map.insert(make_pair(ch, count_char(1, 0)));
        }
        else 
        {
            (record_map[ch].count)[1] += 1;
        }
    }
    std::array<int, 2> temp{};
    for (auto iter = record_map.begin(); iter != record_map.end(); ++iter)
    {
        temp = (iter->second).compare();
        if (temp[0] == 1)
        {
            result += "1:" + std::string(iter->first, temp[1]) + "/";
        }
        else if (temp[0] == 2)
        {
            result += "2:" + std::string(iter->first, temp[1]) + "/";
        }
        else{
            result += "=:" + std::string(iter->first, temp[1]) + "/";
        }
    }
    return result;
}