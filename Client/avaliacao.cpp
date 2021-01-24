#include <stdio.h>

void loop(int n, int maior_a, int maior_f, int ant, int a_inicial, int f_inicial, int a_final, int f_final) {
	int num;
	int i = 0;
	while(i < n) {
		scanf("%d", &num);
		if(i == 0) {
			maior_a = num;
			a_inicial = i;
			a_final = i;
		} else {
			if(ant >= num) {
				if(maior_f < maior_a) {
					maior_f = maior_a;
					f_inicial = a_inicial;
					f_final = a_final;
				}
				maior_a = num;
				a_inicial = i;
			} else {
				maior_a += num;
				a_final = i;
			}
		}
		ant = num;
		i++;
	}
	if(maior_f < maior_a) {
		maior_f = maior_a;
		f_inicial = a_inicial;
		f_final = a_final;
	}
	printf("%d %d %d\n", f_inicial + 1, f_final + 1, maior_f);
}

int main() {

	int n;
	scanf("%d", &n);
	loop(n, 0, 0, 0, 0, 0, 0, 0);
	return 0;
} 