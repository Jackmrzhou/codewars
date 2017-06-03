#include <iostream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
class Negabinary{
public:
  static std::string ToNegabinary(int i);
  static int ToInt(std::string s);
};
int main(void)
{
    std::cout << Negabinary::ToInt("1110") << std::endl;
    std::cout << Negabinary::ToNegabinary(6) << std::endl;
    return 0;
}
std::string Negabinary::ToNegabinary(int i)
{
    if (i == 0)
        return std::string("0");
    std::stringstream stream;
    std::string result;
    int temp = 0;
    while (i != 0)
    {
        temp = abs(i) % -2;
        stream << temp;
        i = (i - temp) / -2;
    }
    result = stream.str();
    reverse(result.begin(), result.end());
    return result;
}
int Negabinary::ToInt(std::string s)
{
    int result=0;
    for (std::string::size_type i = 0; i != s.size(); ++i)
    {
        if (s[i]=='1')
            result += (int)pow(-2, s.size() - i - 1);
    }
    return result;
}