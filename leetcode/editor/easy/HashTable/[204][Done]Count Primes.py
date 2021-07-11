# Count the number of prime numbers less than a non-negative number, n. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 0
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: n = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 5 * 106 
#  
#  Related Topics Hash Table Math 
#  👍 2871 👎 751


# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class Solution:
    # Brutal Force:
    # def countPrimes(self, inputNumber: int) -> int:
    #     primes = set()
    #     for number in range(2, inputNumber):
    #         isNotPrime = False
    #         for prime in primes:
    #             if number % prime == 0:
    #                 isNotPrime = True
    #                 break
    #         if isNotPrime is False:
    #             primes.add(number)
    #     return len(primes)

    def countPrimes(self, n) -> int:
        # Use Sieve of Eratosthenes ( https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes )
        # Cost : Space Complexity will be O(n)
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    # If n = 10, the boolean list will be:
    # [False, False, True, True, True, True, True, True, True, True] before the iteration.
    # After looping on i = 2, the boolean list will be:
    # [False, False, True, True, False, True, False, True, False, True].
    # After looping on i = 3, the boolean list will be:
    # [False, False, True, True, False, True, False, True, False, False].
    # So the answer for n = 10 is 4.
    # Hope this helps you a little bit.


# leetcode submit region end(Prohibit modification and deletion)
class TestCase(unittest.TestCase):

    def testIsValid_1(self):
        inputNumber = 10
        expectedResult = 4

        self.assertEqual(Solution().countPrimes(inputNumber), expectedResult)

    def testIsValid_2(self):
        inputNumber = 0
        expectedResult = 0

        self.assertEqual(Solution().countPrimes(inputNumber), expectedResult)

    def testIsValid_3(self):
        inputNumber = 1
        expectedResult = 0

        self.assertEqual(Solution().countPrimes(inputNumber), expectedResult)

    def testIsValid_4(self):
        inputNumber = 50
        expectedResult = 15

        self.assertEqual(Solution().countPrimes(inputNumber), expectedResult)

    def testIsValid_5(self):
        inputNumber = 499979
        expectedResult = 41537

        self.assertEqual(Solution().countPrimes(inputNumber), expectedResult)


if __name__ == "__main__":
    unittest.main()
