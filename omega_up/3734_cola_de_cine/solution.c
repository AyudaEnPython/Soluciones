/** AyudaEnPython: https://www.facebook.com/groups/ayudapython
 * 
 *    Estatus    : AC 
 *    Porcentaje : 100.00%
 *    Memoria    : 1.60 MB
 *    Tiempo     : 0.00s
*/

#include <stdio.h>

int main() {
    int m = 0, n = 0, t = 0, c = 0, p = 0;
    while (n != -1) {
        scanf("%i", &n);
        c++;
        if (c == 1) m += n;
        t += n;
        if (n != 0) p += n;
        if (p > m) m = p;
        p--;
    }
    t += 1;
    printf("%i %i", t, m);
    return 0;
}