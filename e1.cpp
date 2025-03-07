// Téo Sobrino Alves - 12557192 ex1, Lab de Alg. Avançados

#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void commentAutomation(void)
    {
        int num_sites;
        int num_cmds;

        cin >> num_sites;
        cin >> num_cmds;

        vector<string> site_names(num_sites);
        vector<string> site_ips(num_sites);

        unordered_map<string, string> dns;

        string site;
        string ip;
        for(int i = 0; i < num_sites; i++){
            cin >> site;
            cin >> ip;
            ip += ';';
            dns[ip] = site;
        }

        string cmd;
        for(int i = 0; i < num_cmds; i++){
            cin >> cmd;
            cin >> ip;
            cout << cmd << ' ' << ip << ' ' << '#' << dns[ip] << endl;
        }

        return;
    }

};

int main()
{
    Solution sol;
    sol.commentAutomation();

    return 0;
}