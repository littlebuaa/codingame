#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
typedef vector<int> mylist;

void conway(mylist& seed)
    {
        mylist temp(seed);
        int Len = temp.size();
        temp.push_back(-1);
        int count =1;
        seed.clear();
        
        for(int i=0;i<Len;i++)
        {
            if (temp[i]==temp[i+1])
                count+=1;
            else
            {   seed.push_back(count);
                seed.push_back(temp[i]);
                count =1;
            }
        }
        
    }

int main()
{
    int R;
    cin >> R; cin.ignore();
    int L;
    cin >> L; cin.ignore();

    mylist x;
    x.push_back(R);
    
    for(int i = 0;i<L-1;i++)
        conway(x);

    string s ="";
    for(int i =0;i<x.size();i++)
        s+= to_string(x[i])+ " ";
    
    s.pop_back();
    
    cout << s << endl;
}
