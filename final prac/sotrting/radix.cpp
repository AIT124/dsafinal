#include<bits/stdc++.h>
using namespace std;

void radix(int n,int ar[])
{
    int max=0;
    queue<int> q[10];
    for(int i=0;i<n;i++)
    {
        if(ar[i]>max)
        {
            max=ar[i];
        }
    }
    int z=1;
    while(max)
    {
        for(int i=0;i<n;i++)
        {
            int p=ar[i]/z;
            int x=p%10;
            q[x].push(ar[i]);
        }
        z=z*10;
        
        int o=0;
        for(int i=0;i<10;i++)
        {
            int l=q[i].size();
            for(int j=0;j<l;j++)
            {
                ar[o]=q[i].front();
                // cout<<q[i].front()<<"  ";
                q[i].pop();
                o++;
            }
            
        }
        
        cout<<endl;
        max=max/10;
    }
    for(int i=0;i<n;i++)
            {
                cout<<ar[i]<<"  ";
            }
            cout<<endl;
}

int main(){
    int n;cin>>n;
    cout<<"RADIX"<<endl;
    int ar[n];
    for (int i=0;i<n;i++){
        cin>>ar[i];
    }
    radix(n,ar);
}