import math     #this lib is for the function that determines either a number is prime or not
import unittest  #this one I use with selenium as well. 


def is_prime(n):     #This function determines the prime numbers
    if n == 2:   
        return True
    if n % 2 == 0 or n <= 1:    #If the remainder of n/2 equals to 0 or less than 1, number is not prime
        return False
    sqr = int(math.sqrt(n)) + 1     
    for divisor in range(3, sqr, 2):     #iteration over dividers
        if n % divisor == 0:    
            return False
    return True


def list_primes(*args):     #this function gets new list with only prime numbers
    new_list = []
    for i in range(len(args)):  
        if is_prime(args[i]):
            new_list.append(args[i])
    return new_list


class TestPrimes(unittest.TestCase):    #class for the tests

    def test_primeN1(self):
        self.assertEqual(list_primes(1, 2, 3), [2, 3], "Should be 2, 3")
        print(list_primes(1, 2, 3))

    def test_primeN2(self):
        self.assertEqual(list_primes(11, 1, 4, 200, 67, 1000, 281, 500, 449), [11, 67, 281, 449], "Should be 11, 67, 281, 449")
        print(list_primes(11, 1, 4, 200, 67, 1000, 281, 500, 449))

    def test_primeN3(self):
        self.assertEqual(list_primes(6, 1, 4, 100, 120, 155, 175, 256), [], "Should be empty")
        print(list_primes(6, 1, 4, 100, 120, 155, 175, 256))

    def test_primeN4(self):
        self.assertEqual(list_primes(720, 1018, 1117, 562, 857, 900, 1216, 1031), [1117, 857, 1031], "Should be 1117, 857, 1031")
        print(list_primes(6, 1, 4, 1117, 562, 857, 900, 1216, 1031))


unittest.main()