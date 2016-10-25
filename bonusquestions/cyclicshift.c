#include <stdio.h>
int main(){
     int arr[20], i,j,n,m;
     scanf("%d %d",&n, &m);
     m = m%n;
     for(i=0;i<n;i++)
     scanf("%d", arr[i]);
     int newarr[20];
     for(j=0,i=n-m;j<n;j++){
           if(i==n)
           i=0;
           newarr[j] = arr[i];
           i++;}
     for(i=0;i<n;i++)
     printf("%d ", newarr[i]);             
     return 0;
     }
