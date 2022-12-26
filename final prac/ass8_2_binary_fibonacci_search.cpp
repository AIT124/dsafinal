
#include <bits/stdc++.h>
using namespace std;

void binary_search(int arr[],int n, int key)
{
  cout<<"Using Binary Search: "<<endl;
  int comp=0;
   
   int lo=0,hi=n-1;
   while((hi-lo)>1){
      int mid=(hi+lo)/2;
      if(arr[mid]<key){
          lo=mid+1;comp++;
      }
      else if(arr[mid]>key){
          hi=mid-1;comp+=2;
      }
      else {
        comp+=2;
        cout<<"Element found at index "<<mid+1<<endl;
        cout<<"No. of comarisons: "<<comp<<endl;return;
      }
   }
   if(arr[lo]==key){
      cout<<"Element found at index "<<lo+1<<endl;
   }
   else if(arr[hi]==key){
    cout<<"Element found at index "<<hi+1<<endl;
   }
   else{
      cout<<"Element not found in Binary search "<<endl; 
   }
   cout<<"No. of comarisons: "<<comp<<endl;
}

 void fibonacci_search(int arr[],int n,int key)
{
    cout<<"Using Fibonacci Search: "<<endl;
	  int fib=1;
	  int fib1=1;
	  int fib2=0;
	  while(fib<n){
	    fib2=fib1;
	    fib1=fib;
	    fib=fib1+fib2;
	  } 
    cout<<"fib2"<<" "<<"fib1"<<" "<<"fib"<<" "<<"offset"<<" "<<"index"<<" "<<"arr[index]"<<endl;  
	  int offset=0;
	  int index=min(fib2+offset,n);
    int comparisions=0;
    bool value=false;
	  while(fib2>0){
      cout<<fib2<<" "<<fib1<<" "<<fib<<" "<<offset<<" "<<index<<" "<<arr[index-1]<<endl;  
     comparisions++;
      if(fib==2){
         if(arr[index-1]==key){
             cout<<"Key found at index : "<<index<<endl;
            cout<<"Number of comparisons: "<<comparisions<<endl;return;
            }
          else break;

      }
      comparisions++;
     if(arr[index-1]<key){
       fib=fib1;
       fib1=fib2;
       fib2=fib-fib1;
       offset=index;
       index=min(fib2+offset,n);
     }
	   else if(arr[index-1]>key){  
        comparisions++;
	     fib=fib2;
	     fib1=fib1-fib;
	     fib2=fib-fib1;
	     index=min(offset+fib2,n);
	   }
     else{
        comparisions++;
        cout<<"Key found at index : "<<index<<endl;
        cout<<"Number of comparisons: "<<comparisions<<endl;
        return;
     }
	   
	  }
    cout<<"Key Not found"<<endl;
    cout<<"Number of comparisons: "<<comparisions<<endl;
}


signed main()
{

  cout<<"Number of students: ";
  int n;cin>>n;
  int arr[n];
  cout<<"Enter their roll no.s in ascending order: ";
  for(int i=0;i<n;i++){
    cin>>arr[i];
  }
  cout<<"Enter the roll no. to be searched: ";
  int key;cin>>key;

  binary_search(arr,n,key);
  fibonacci_search(arr,n,key);

}

