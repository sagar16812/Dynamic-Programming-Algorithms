#include <iostream>
#include <cmath>

/*
In this code, the isArmstrongNumber() function takes an integer n as input and 
checks whether it is an Armstrong number. It does this by counting the number 
of digits in the original number and then calculating the Armstrong sum. The 
Armstrong sum is obtained by raising each digit to the power of the number of 
digits and adding them together. Finally, the function compares the Armstrong 
sum with the original number to determine if it is an Armstrong number.

In the main() function, the user is prompted to enter a number. The 
isArmstrongNumber() function is called with the entered number, and 
the result is printed accordingly.
*/

using namespace std;

bool isArmstrongNumber(int n) {
    int originalNumber = n;
    int numDigits = 0;
    int armstrongSum = 0;

    // Count the number of digits
    while (originalNumber != 0) {
        originalNumber /= 10;
        numDigits++;
    }

    // Calculate the Armstrong sum
    originalNumber = n;
    while (originalNumber != 0) {
        int digit = originalNumber % 10;
        armstrongSum += pow(digit, numDigits);
        originalNumber /= 10;
    }

    return (armstrongSum == n);
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;

    if (isArmstrongNumber(number))
        cout << number << " is an Armstrong number." << endl;
    else
        cout << number << " is not an Armstrong number." << endl;

    return 0;
}

