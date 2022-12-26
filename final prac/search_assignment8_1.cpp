

#include <bits/stdc++.h>
using namespace std;

void linear_search(int arr[],int n,int key){
    cout<<"Using Linear Search:"<<endl;
    int comp=0;
    for(int i=0;i<n;i++){
        comp++;
        if(arr[i]==key){
            cout<<"Key found at index: "<<i+1<<endl;
            cout<<"No. of comparisons: "<<comp<<endl;
            return;
        }
    }
    cout<<"Key not found"<<endl;
    //cout<<"No. of comparisons: "<<comparisons<<endl;
}

void sentinel_search(int arr[],int n,int key){
    cout<<"Using Sentinel Search"<<endl;
    int comp=1;
    arr[n]=key;
    int i;
    for(i=0;arr[i]!=key;i++){comp++;}
    if(i==n){
        cout<<"Key not found"<<endl;
    }
    else{
        cout<<"Key found at index: "<<i+1<<endl;
    }
    //cout<<"No. of comparisons: "<<comparisons<<endl;
   
}

signed main()
{

  cout<<"Number of students: ";
  int n;cin>>n;
  int arr[n+1];
  cout<<"Enter their roll no.s: ";
  for(int i=0;i<n;i++){
    cin>>arr[i];
  }
  cout<<"Enter the roll no. to be searched: ";
  int key;cin>>key;

  linear_search(arr,n,key);
  sentinel_search(arr,n,key);

}