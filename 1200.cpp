#include "includes.h"


class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        vector<int> arr1= arr;
        int absdif = INT_MAX;
        int curdif = 0;
        vector<int> vec1 = {};
        vector<vector<int>> vec2 ={};
        sort(arr1.begin(), arr1.end());
        
        for(int i = 0; i< arr1.size()-1; i++){
            curdif = abs(arr1[i] - arr1[i+1]);
            if(curdif<absdif){
                absdif = curdif;
            }
        }
        
        for(int i =0;i<arr1.size()-1; i++){
            if(abs(arr1[i]-arr1[i+1]) == absdif){
                vec1.push_back(arr1[i]);
                vec1.push_back(arr1[i+1]);
                vec2.push_back(vec1);
            }
            vec1.clear();
        }



        return vec2;

    }
};

int main(void){
    vector<int> arr = {4,2,1,3};
    Solution sol;
    vector<vector<int>> res = sol.minimumAbsDifference(arr);
    for(auto vec1 : res){
        for(auto vec2 : vec1){
            cout << vec2 << " ";
        }
        cout<<"-";
    }
}