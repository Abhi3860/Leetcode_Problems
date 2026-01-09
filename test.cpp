#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main(void){
    vector<int> one = {1,2,3,4,5};
    vector<int> two = {6,7,8,9,0};
    int size1 = one.size();
    int size2 = two.size();
    long totalPairs = size1*size2;
    
    for(long i =0; i<totalPairs; ++i){
        int index1 = i/size2;
        int index2 = i%size2;
        cout << one[index1]<< ","<< two[index2]<< endl;
    }
}