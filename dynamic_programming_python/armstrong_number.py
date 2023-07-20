'''
In this code, the function is_armstrong_number() takes an integer n as input and 
checks whether it is an Armstrong number. It does this by converting the number 
to a string and iterating over its digits. For each digit, it raises it to the 
power of the total number of digits and adds it to the armstrong_sum. Finally, it 
compares the armstrong_sum with the original number n to determine if it is an 
Armstrong number.

You can test the code by entering a number, and it will output whether it is an 
Armstrong number or not.
'''
def is_armstrong_number(n):
    # Convert the number to a string to iterate over its digits
    digits = str(n)
    num_digits = len(digits)
    armstrong_sum = 0

    for digit in digits:
        armstrong_sum += int(digit) ** num_digits

    return armstrong_sum == n

# Example usage
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

