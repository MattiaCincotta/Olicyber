#include <stdio.h>
#include <string.h>

int pair_strings(char *a1, char *a2, char *a3, int a4) {
    int v4; // eax
    char *v5; // rcx
    int v6; // eax
    int v7; // eax
    int result = 0; // rax
    int v10 = 0; // [rsp+20h] [rbp-Ch]
    int v11 = 0; // [rsp+24h] [rbp-8h]
    unsigned int v12 = 0; // [rsp+28h] [rbp-4h]

    while (1) {
        if (v11 >= a4) {
            result = v12;
            if ((int)v12 >= a4)
                break;
        }

        if ((v10 & 1) != 0) {
            v4 = v12++;
            v5 = a3 + v4;
        } else {
            v7 = v11++;
            v5 = a2 + v7;
        }

        v6 = v10++;
        a1[v6] = *v5;
    }

    return result;
}

void make_serial(const char *user_id) {
    char a1[48];  // Array di destinazione
    char a2[48];  // Array di destinazione
    int i = 0;

    // Copia user_id nell'array a1
    for (i = 0; i < strlen(user_id); i++) {
        a1[i] = user_id[i];
    }

    printf("a1: ");
    for (i = 0; i < strlen(user_id); i++) {
        printf("%c", a1[i]);
    }
    printf("\n");

    // Esegui le operazioni pair_strings con diverse porzioni di a1
    pair_strings(a2, &a1[18], &a1[9], 8);  // Copia 8 caratteri da a1[18:] e a1[9:18] in a2
    printf("prova A: ");
    for (i = 0; i < 16; i++) {
        printf("%c", a2[i]);
    }
    printf("\n");
    
    pair_strings(&a2[16], &a1[0], &a1[18], 8);  // Copia 8 caratteri da a1[:9] e a1[18:] in a2[16:]
    printf("prova B: ");
    for (i = 0; i < 16; i++) {
        printf("%c", a2[i]);
    }
    printf("\n");

    pair_strings(&a2[32], &a1[9], &a1[0], 8);  // Copia 8 caratteri da a1[9:] e a1[:9] in a2[32:]
    printf("prova C: ");
    for (i = 0; i < 16; i++) {
        printf("%c", a2[i]);
    }
    printf("\n");

    // Stampa la chiave finale
    printf("Chiave finale: ");
    for (i = 0; i < 48; i++) {
        printf("%c", a2[i]);
    }
    printf("\n");
}

int main() {
    const char *user_id = "ShMMWiYL-DM4Kireh-L9FRsU3A";  // User ID
    make_serial(user_id);
    return 0;
}
