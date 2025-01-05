#include<iostream>
using namespace std;

int main() {
    int x;
    cout << "Please enter the number you got: ";
    cin >> x;
    if(x == 5){
        cout <<"Decryption successful" << endl; 
    }
    else{
        cout << "Wrong Answer obtained, model inaccurate!!" << '\n'; 
    }

    return 0;
}