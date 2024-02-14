# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:00:37 2024

@author: niran
"""

def partialPalindrome(s, n):
  """
  Checks if the string s contains a substring of length n that is a palindrome.

  Args:
      s: The input string.
      n: The length of the palindrome to check for.

  Returns:
      True if there is a palindrome of length n in s, False otherwise.
  """

  for i in range(len(s) - n + 1):
    substring = s[i:i+n]
    if substring == reverse(substring):
      return True
  return False

# Example usage
print(partialPalindrome("AGTTGCC", 4))  # True
print(partialPalindrome("AGTTGCC", 3))  # False
