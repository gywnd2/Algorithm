#include <iostream>
using namespace std;

int main(){
    int i, j, temp;
    int arr[10]={5,7,2,3,8,10,4,9,1,6};
    for(i=0; i<9; i++){
        j=i;
        while(j>=0 && arr[j]>arr[j+1]){
            temp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
            j--;
        }
    }
    for(i=0; i<10; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}