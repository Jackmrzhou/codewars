#include <vector>
#include <iostream>
using namespace std;

typedef unsigned char u8;
struct rgb
{
    u8 RGB[3];
};
vector<u8> processImage(const vector <u8> &imageData,int height,int width, vector <vector <float>> weights) 
{
    int mH = weights.size(),mW = weights[0].size();
    vector <u8> result;
    rgb newimg[height][width];
    for (int i = 0; i < height; ++i)
        for (int j = 0; j < width; ++j)
        {
            newimg[i][j] = rgb{imageData[(i*height+j)*3],
                                imageData[(i*height+j)*3+1],
                                imageData[(i*height+j)*3+2]};
        }
    
    for (int i = 0; i < height; ++i)
        for (int j = 0; j< width; ++j)
            for (int k = 0; k!=3; ++k)
            {
                u8 pixel_matrix[mH][mW];
                for (int r=0; r<mH;++r)
                    for (int c=0;c<mW;++c)
                    {
                        int rr = i-mH/2+r,cc= j-mW/2+c;
                        if (rr < 0)
                            rr = 0;
                        if (cc < 0)
                            cc = 0;
                        if (rr >= height)
                            rr = height-1;
                        if (cc>= width)
                            cc = width-1;
                        pixel_matrix[r][c] = newimg[rr][cc].RGB[k];
                    }
                float newpixel = 0;//don't use u8
                for (int r=0; r<mH;++r)
                    for (int c=0;c<mW;++c)
                        newpixel += pixel_matrix[r][c] * weights[r][c];
                if (newpixel < 0)
                    newpixel = 0;
                if (newpixel > 255)
                    newpixel = 255;
                result.push_back((u8)newpixel);
            }
    return result;
}

int main()
{
    auto res = processImage ({0,0,0,0,0,0,0,0,0,255,255,255},
                            2, 2,
                            {{0.2,0,0},{0,0.2,0.2},{0,0.2,0.2}});
    for (auto i : res)
        cout <<(int)i<<','<<endl;
    return 0;
}