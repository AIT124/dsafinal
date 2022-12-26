#include<bits/stdc++.h>
using namespace std;


int com=0,shift=0;
void insertion_sort(int arr[],int n){
	
	for(int	i=1;i<n;i++){
		int ans=i,temp=arr[i];
		for(int j=i-1;j>=0;j--){
			com++;
		if(temp<arr[j]){
			
			arr[j+1]=arr[j];
			ans=j;	
			shift++;
			//cout<<ans<<endl;
		
		}
		else{break;}

		}
		arr[ans]=temp;
		if(ans!=i){
			shift++;
		}
		for(int i=0;i<n;i++){
			cout<<arr[i]<<" ";
		}
		cout<<endl;
	}
	
	
	

}




int main(){
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	insertion_sort(arr,n);
	cout<<"No of comparison :"<<com<<endl;
	cout<<"No of shifts :"<<shift<<endl;
 }
