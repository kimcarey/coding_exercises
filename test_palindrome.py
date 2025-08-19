"""
Problem: Valid Palindrome
Given a string, return True if it's a palindrome (reads the same forwards and backwards),
considering only alphanumeric characters and ignoring case.
"""

def is_palindrome(s):
    # Step 1: Clean the string
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    #  Step 2: Set indices based on CLEANED string
    left_index = 0
    right_index = len(cleaned) - 1

    # Step 3: Move pointers and check if each char is the same
    while left_index < right_index:
        if cleaned[left_index] == cleaned[right_index]:
            left_index += 1
            right_index -= 1
        else:
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))