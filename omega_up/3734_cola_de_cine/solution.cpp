/** AyudaEnPython: https://www.facebook.com/groups/ayudapython
 * 
 *    Estatus    : AC
 *    Porcentaje : 100.00%
 *    Memoria    : 3.47 MB
 *    Tiempo     : 0.00s
*/

#include <bits/stdc++.h>

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int m = 0, n = 0, t = 0, c = 0, p = 0;
  
  while (n != -1) {
      std::cin >> n;
      c++;
      if (c == 1) m += n;
      t += n;
      if (n != 0) p += n; 
      if (p > m) m = p;
      p--;
    }
  t += 1;
  std::cout << t << " " << m;
  return 0;
}