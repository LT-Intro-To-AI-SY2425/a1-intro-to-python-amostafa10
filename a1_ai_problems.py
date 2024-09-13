# Complete your individualized AI problems here

# Reverse a String: Write a function reverse_string(s) that takes a string s and returns the string in reverse order.

def reverse_string(s: str):
    output = ""
    for i in range(len(s) - 1, -1, -1):
        output += s[i]
    return output

assert reverse_string("hello") == "olleh", "reverse did not work"

# Sum of Even Numbers: Write a function sum_of_evens(numbers) that takes a list of integers and returns the sum of all the even numbers in the list.

def sum_of_evens(numbers):
    output = 0
    for x in numbers:
        if x % 2 == 0:
            output += x
    return output

assert sum_of_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "sum_of_evens did not work"

# Count Vowels: Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string s.

vowels = [
    "a",
    "e",
    "i",
    "o",
    "u"
]

def count_vowels(s):
    output = 0
    for x in s:
        if x in vowels:
            output += 1
    return output

assert count_vowels("The quick brown fox jumps over the lazy dog") == 11, "count_vowels did not work"