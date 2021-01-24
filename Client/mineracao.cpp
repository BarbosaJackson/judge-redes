#include <stdio.h>

int main() {
	int n, arr[100], entrada, i;
	scanf("%d", &n);
	for(i = 0; i < n; i++) 
		scanf("%d", &arr[i]);
	scanf("%d", &entrada);
	while(arr[entrada] != -1) {
		entrada = arr[entrada];
	}
	printf("%d\n", entrada);
	return 0;
}