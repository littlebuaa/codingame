#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void gogogo(bool & x, int pair [2], int listpair[][2], int n)
    {   x = false;
        for (int i =0;i<n;i++)
        {
            if (pair[1] ==listpair[i][0]){
                x = true;
                pair[0] = listpair[i][0];
                pair[1] = listpair[i][1];
                break;
            } 
        }
    };

int main()
{
	int n;
	cin >> n;
	int relation[n][2];
	
	for (int i = 0; i < n; i++) {	
	    int a = 0,b=0;
	    cin>> a >> b;
	    relation[i][0] = a;
	    relation[i][1] = b;
	    cin.ignore();
	}


int num[n]; // For storing the total steps of every loop

int tem[2];

for (int i = 0; i < n; i++) {
    int numTemp = 2;
    tem[0] = relation[i][0];
    tem[1] = relation[i][1];
    
    bool T = true;
    while(T)
    {   gogogo(T,tem,relation,n);
        if(T)
            numTemp+=1;
    }
    
    num[i]= numTemp;
}

sort(num,num+n);// Find longest steps


cout << num[n-1] <<endl;
	
return 0;
}
