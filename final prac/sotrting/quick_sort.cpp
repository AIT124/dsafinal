#include<bits/stdc++.h>
using namespace std;

int partition(int arr[],int start,int end){
	int pivot;
	pivot=arr[start];
	int i=start+1,j=end;
	while(i<=j ){
		while(arr[i]<=pivot && i<=end){
			i++;	
		}
		while(arr[j]>pivot && j>=0){
			j--;	
		}
		if(i<j){
			swap(arr[i],arr[j]);	
		}
		
	
	}
       swap(arr[j],arr[start]);
	return j;

}
void quicksort(int arr[],int start,int end){
		for(int i=0;i<end+1;i++){
			cout<<arr[i]<<" ";
		}
		cout<<endl;
	if(start<end){
		int x=partition(arr,start,end);
		
		quicksort(arr,start,x-1);


		quicksort(arr,x+1,end);	
		

	}
}
int main(){
	
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	quicksort(arr,0,n-1);
	}

