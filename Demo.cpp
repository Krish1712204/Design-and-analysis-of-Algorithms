#include<iostream>
using namespace std;
int main(){
    int a[20],size,flag=1,count=0,lim=0;
    cout<<"Enter the max size :\n";
    cin>>size;
    cout<<"enter stream of 1's and  0's which has length "<<size;
    do{
        lim=0;
        flag=1;
        for(int i=0;i<size;i++)
            cin>>a[i];
        for(int i=0;i<size;i++){
            if(a[i-1]== 1 && a[i]==0){
                flag=0;
            }
            if(flag==0 && a[i]==1){
                cout<<"invalid bit stream\n";
                lim=1;
                break;
            } 
        
        }
        
        
        if(lim==1){
            cout<<"Enter new bit stream \n";
        }
    }
    while(lim==1);

    for(int i=0;i<size;i++){
        if(a[i]==0 && flag==0)
            count++;
        
    }
    cout<<"The number of 0's are :"<<count;

    return 0;
}