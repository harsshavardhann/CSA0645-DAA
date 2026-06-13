def is_palindrome(word):
    return word == word[::-1]

def first_palindrome(words):
    for word in words:
        if is_palindrome(word):
            return word
    return ""

# Example 1
words = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindrome(words))

# Example 2
words = ["notapalindrome", "racecar"]
print(first_palindrome(words))
