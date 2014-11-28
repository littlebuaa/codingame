#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath> 

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int N;
    cin >> N; cin.ignore();
    vector<long>Xcor(N);
    vector<long>Ycor(N);
    long sum =0;
    for (int i = 0; i < N; i++) {
        int X;
        int Y;
        cin >> X >> Y; cin.ignore();
        Xcor[i]= X;
        Ycor[i]=Y;
        sum += Y;
    }
    
    /* Find the best Y value, to decide the Main Cable. */
    /* Most near the Mean value of all the Y coordinate */
    double moyen = sum/N;
    vector<double> New(N);
    
    for(long i=0;i<N;i++)
        {
            New[i] = abs((Ycor[i]) - moyen);
        }
    
    double temp = *min_element(New.begin(),New.end());
    
    /*Find the index of the best Y in the Y coordinate vector  */
    vector<double>::iterator dex;
    dex = find(New.begin(),New.end(),temp);
    int index = dex- New.begin();
    
    
    // long index = 0;
    // for (long i =0;i< N;i++)
    //     {if((New[i])==temp)
    //         {index =i;
    //          break;}}
    
    /* calculate the total Vertical distance*/ 
    sum =0;
    for(long i =0;i<N;i++)
    {
        sum += abs(Ycor[i] - Ycor[index]);
    }
    
    /*caculate the total Horizontal distance*/
    sort(Xcor.begin(),Xcor.end());
    long D = Xcor[N-1]- Xcor[0];
    
    
    D += sum;
  
    cout << D << endl;
}
