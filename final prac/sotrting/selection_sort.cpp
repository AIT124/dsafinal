#include<bits/stdc++.h>
using namespace std;


int swa=0,comp=0,it=0;
void selection_sort(int arr[],int n){
	for(int	i=0;i<n;i++){
		int minn=i;
		for(int j=i+1;j<n;j++){
			comp++;
			if(arr[j]<arr[minn]){
				minn=j;
				}


		}
		if(arr[i]!=arr[minn]){
			swap(arr[i],arr[minn]);
		swa++;}
	it++;
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
	selection_sort(arr,n);
	cout<<"No of swaps :"<<swa<<endl;
	cout<<"No of passes :"<<it<<endl;
	cout<<"no of comparision:"<<comp<<endl;




}
