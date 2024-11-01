//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:
    int rowWithMax1s(vector<vector<int> > &arr) {
        // code here
        int zero=0;
        vector<int> v;
        bool flag=false;
        for(int i=0;i<arr.size();i++)
        {
            zero=0;
            for(int j=0;j<arr[i].size();j++)
            {
                if(arr[i][j]==1)
                {
                    flag=true;
                    zero++;
                }
            }
            v.push_back(zero);
        }
        int index=0;
        for(int i=1;i<v.size();i++)
        {
            if(v[index]<v[i])
            index=i;
        }
        if(!flag) return -1;
        return index;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int> > arr(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> arr[i][j];
            }
        }
        Solution ob;
        auto ans = ob.rowWithMax1s(arr);
        cout << ans << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends