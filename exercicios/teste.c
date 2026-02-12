#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Função solicitada: findNumber
 *
 * Parâmetros:
 * 1. arr_count: O tamanho do array
 * 2. arr: O ponteiro para o array de inteiros
 * 3. k: O número que estamos procurando
 */
char* findNumber(int arr_count, int* arr, int k) {
    // Percorre cada elemento do array
    for (int i = 0; i < arr_count; i++) {
        // Verifica se o elemento atual é igual a k
        if (arr[i] == k) {
            // Se encontrou, retorna "YES"
            return "YES";
        }
    }
    
    // Se o loop terminou e não retornou nada, significa que k não está no array
    return "NO";
}
