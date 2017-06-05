#include <iostream>
#include <vector>
bool valid_braces(std::string braces);
int main(void)
{
    bool result = valid_braces(std::string("{([{}][])}"));
    std::cout << result << std::endl;
    return 0;
}
bool valid_braces(std::string braces) 
{
    auto lenth = braces.size();
    if (lenth % 2)
        return false;
    std::vector<char> brace_vector{};
    for (auto ch : braces)
    {
        if (ch=='{' || ch == '[' || ch=='(')
            brace_vector.push_back(ch);
        else 
        {
            if (brace_vector.empty())
                return false;
            auto temp = *(brace_vector.end() - 1);
            if (ch==')' && temp=='(' || ch =='}' && temp=='{' ||\
                ch == ']' && temp=='[')
                brace_vector.pop_back();
            else
                return false;
        }
    }
    return true;
}