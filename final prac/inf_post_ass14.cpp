#include<bits/stdc++.h>
using namespace std;

int precedance(char c){
    if(c=='^'){
        return 3;
    }
    else if(c=='*'|| c=='/'){
        return 2;
    }
    else if (c=='+'||c=='-'){
        return 1;

    }
    else {
        return -1;
    }

}

void infixtopostfix(string s){
    stack<char>st;
    string result;

    for(int i=0;i<s.length();i++){
        if((s[i]>='0' && s[i]<='9')||(s[i]>='a' && s[i]<='z')||(s[i]>='A' && s[i]<='Z' )){
            result+=s[i];
        }
        else if (s[i]=='('){
            st.push(s[i]);
        }
        else if (s[i]==')'){
            while(!st.empty() && st.top()!='('){
                result+=st.top();
                st.pop();
            }
            if (!st.empty()){
                st.pop();
            }
        }
        else{
            while(!st.empty() && precedance(st.top())>=precedance(s[i])){
                result+=st.top();
                st.pop();
            }
            st.push(s[i]);
        }
    }
    while(!st.empty()){
        result+=st.top();
        st.pop();
    }
    cout<<result<<endl;
}
int postfixevaluation(string s){
    stack<int>st;

    for(int i=0;i<s.length();i++){
        if(s[i]>='0' && s[i]<='9'){
            st.push(s[i]-'0');
        }
        else{
            int opt2 =st.top();
            st.pop();
            int opt1 =st.top();
            st.pop();
       
        switch(s[i]){
            case '+':
                st.push(opt1 + opt2);
                break;
            case '-':
                st.push(opt1 -opt2);
                break;
            case '*':
                st.push(opt1*opt2);
                break;
            case '/':
                st.push(opt1/opt2);
                break;
            case '^':
                st.push(pow(opt1,opt2));
                break;
            }
        }
    }
    return st.top();
}
int main()
{   
    int ch;
    while(1){
        cout<<"1.infix to post fix \n2.evalution \n3.exit";
        cout <<"\nenetr your choice:";
        cin>>ch;
        if (ch==1){
            string exp ;
            cout<<"enter the infix expression : ";
            cin>>exp;
            cout<<"postfix expression is : ";
            // Function call
            infixtopostfix(exp);
        }
        else if(ch==2){
            string some;
            cout<<"eneter the postfix operation for evalution:";
            cin>>some;
            cout<<"\npostfix evalution is:";
            cout<<postfixevaluation(some)<<endl;
        }
        else{exit(0);}
    }
    
    return 0;
}