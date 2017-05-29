#include <iostream>
std::string decrypt(std::string encryptedText, int n);
std::string encrypt(std::string text, int n);
int main(void)
{
    std::string text("This is a test!");
    auto s = encrypt(text, 2);
    std::cout << s << std::endl;
    s = decrypt(s, 2);
    std::cout << s << std::endl;
    return 0;
}
std::string encrypt(std::string text, int n)
{
    while(--n >= 0)
        for (std::string::size_type i = 0; i != (text.size()+1)/2; ++i)
        {
            text += text[i];
            text.erase(i, 1);
        }
    return text;
}
std::string decrypt(std::string encryptedText, int n)
{
    while(--n >= 0)
    {
        auto it = encryptedText.begin();
        for (auto i = encryptedText.size() / 2; i != encryptedText.size(); ++i)
        {
            it = encryptedText.insert(it, encryptedText[i]);
            it += 2;
            encryptedText.erase(i+1, 1);
        }
    }
    return encryptedText;
}