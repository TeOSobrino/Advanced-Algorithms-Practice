// Téo Sobrino Alves - 12557192 ex2, Lab de Alg. Avançados

#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:

    void wc(void)
    {
        map<string, int> word_counter;

        string word = "";
        int wn = 0;
        char c;
        c = getchar();
        while(c >= ' ' && c <= 'z'){

            if(c >= 'A' && c <= 'Z'){
                c += 32;
            }

            if(c >= 'a' && c <= 'z' ){
                word += c; 
            }

            else if(c >= ' ' && c <= 'z' && word != ""){
                word_counter[word]++; 
                word = "";
                wn++;
            }

            c = getchar();
        }

        cout << wn << endl;
        
        int sz = word_counter.size();
        int i = 0;
        for(auto w = word_counter.begin(); i < sz; ++w, ++i){

            if(i == sz-1) cout << w->first << endl;
            else cout << w->first << ", ";
        
        }
        

        for(auto w = word_counter.begin(); w != word_counter.end(); w++){
            cout << w->first << ' ' << w->second << endl;
        }

    }
};

int main(void)
{
    Solution sol;
    sol.wc();

    return 0;
}