#include <string>
#include <iostream>
std::string to_camel_case(std::string text);
int main(void)
{
    std::string text("The_Stealth_Warrior");
    std::cout << to_camel_case(text) << std::endl;
    return 0;
}
std::string to_camel_case(std::string text) 
{
    std::string new_string;
    for (auto i = text.begin(); i != text.end(); ++i)
    {
        if (*i == '-' || *i=='_')
            *(i + 1) = toupper(*(i + 1));
        else
            new_string += *i;
    }
    return new_string;
}