"""
The approach: Use a counter instead of a stack.
For each ( add 1, for each ) subtract 1. If you ever go negative or don't end at 0, it's invalid.
"""

def is_valid_simple(s):
    # Only contains '(' and ')'
    # Return True if properly balanced
    count = 0

    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


print(is_valid_simple("()"))
print(is_valid_simple("()()"))
print(is_valid_simple("(())"))
print(is_valid_simple("(()"))
print(is_valid_simple("())"))
print(is_valid_simple(")("))