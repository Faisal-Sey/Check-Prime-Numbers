

from numpy import Infinity


def check_prime_numbers(n) -> bool:
    divisibles = []
    for i in range(1, n+1):
        if n % i == 0:
            divisibles.append(i)
    
    if len(divisibles) == 2:
        if divisibles[0] == 1 and divisibles[1] == n:
            return "prime number"
        else:
            return "not prime number"
    else:
        return "not prime number"

number = int(input("Enter number: "))
print(check_prime_numbers(number))