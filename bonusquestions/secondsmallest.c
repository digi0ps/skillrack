#include <stdio.h>
int main(){
	int n,i, arr[100];
	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%d", &arr[i]);
	int key, j;
	for(i=1;i<n;i++){
		key = arr[i];
		j = i-1;
		while(j>=0 && arr[j]>key){
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
	printf("%d", arr[1]);
	return 1;
}
