#include <bits/stdc++.h>

using namespace std;

// Complete the factorial function below.
int factorial(int n) {
    if (n==1 || n==0){
        return 1;
    }else{
        return n*factorial(n-1);
    }
    