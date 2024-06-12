class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> s;
        vector<int> sol(temperatures.size());
        for(int i = 0 ; i < temperatures.size() ; ++i){
            int t = temperatures[i];
            while(!s.empty() && temperatures[i] > temperatures[s.top()]){
                sol[s.top()] = i - s.top();
                s.pop();
            }
            s.push(i);
        }
        return sol;
    }
};