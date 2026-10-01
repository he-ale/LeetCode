#include <string>
#include <stack>

using namespace::std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for(char c : s){
            if(c=='(' || c=='[' || c=='{')
            {
                myStack.push(c);
            }else{
                if(myStack.empty())
                {
                    return false;
                }else{
                    char a= myStack.top();
                    if(a=='(' && c==')')
                    {
                        myStack.pop();
                    }else if (a=='[' && c==']')
                    {
                        myStack.pop();
                    }else if (a=='{' && c=='}')
                    {
                        myStack.pop();
                    }else{
                        return false;
                    }                    
                }
            }
        }
        return myStack.empty();
    }
};