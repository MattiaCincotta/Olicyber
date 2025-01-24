//Nel problema non avendo un parametro passato a rand() sarà di default 0 e perciò il risultato sarà sempre lo stesso

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void simulate_getPass() {
    int i, v2;
    char *v3;

    v2 = rand() % 16 + 5;
    v3 = (char *)malloc(v2 + 1);

    for (i = 0; i < v2; ++i) {
        v3[i] = rand() % 42 + 48;
    }
    v3[v2] = '\0';

    printf("Password simulata: %s\n", v3);
    free(v3);
}

int main() {
    simulate_getPass();
    return 0;
}
