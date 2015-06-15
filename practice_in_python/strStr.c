// AAACAAAA
// 01201233
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void computeLPSArray(char *pat, int M, int *lps)
{
    int len = 0;  // lenght of the previous longest prefix suffix
    int i;
 
    lps[0] = 0; // lps[0] is always 0
    i = 1;
 
    // the loop calculates lps[i] for i = 1 to M-1
    while (i < M)
    {
       if (pat[i] == pat[len])
       {
         lps[i++] = ++len;
       }
       else // (pat[i] != pat[len])
       {
         if (len != 0)
         {
           // This is tricky. Consider the example AAACAAAA and i = 7.
           len = lps[len-1];
 
           // Also, note that we do not increment i here
         }
         else // if (len == 0)
         {
           lps[i] = 0;
           i++;
         }
       }
    }
}

void computeNext(char *pat, int* next, int m){
  next[0] = -1;

}

int strStr(char* haystack, char* needle) {
    char* h = haystack;
    char* p, *q;
    while(*h != '\0'){
        q = needle;
        p = h;
        while(*p == *q){
            p++;
            q++;
            if (*q == '\0'){
                return h-haystack;
            }
        }
        h++;
    }
    return -1;
}

int main(){
    char * pat = "AAACAAAA";
    int m = strlen(pat);
    int * lps = (int*)malloc(m*sizeof(int));
    computeLPSArray(pat,m,lps);
    for (int i =0;i<m;i++){
      printf("%d\t", lps[i]);
    }
    return 0;
}