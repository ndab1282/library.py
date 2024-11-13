#V00701282 NeVaeh Dabney-Rich 

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"
#Checks if all characters in s are in ASCII_LOWERCASE or ASCII_UPPERCASE.
def is_alpha(s):
    for char in s:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True
#Checks if all characters in s are in DECIMAL_DIGITS.
def is_digit(s):
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True
#Converts each uppercase letter in s to its corresponding lowercase letter.
def to_lower(s):
    result = ""
    for char in s:
        found = False
        for i in range(len(ASCII_UPPERCASE)):
            if char == ASCII_UPPERCASE[i]:
                result += ASCII_LOWERCASE[i]
                found = True
                break
        if not found:
            result += char
    return result
#Converts each lowercase letter in s to its corresponding uppercase letter.
def to_upper(s):
    result = ""
    for char in s:
        found = False
        for i in range(len(ASCII_LOWERCASE)):
            if char == ASCII_LOWERCASE[i]:
                result += ASCII_UPPERCASE[i]
                found = True
                break
        if not found:
            result += char
    return result
#Finds the index of the first occurrence of char in s.
def find_chr(s, char):
    if len(char) != 1:
        return -1
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1
print(find_chr('hello', 'l'))
#Finds the index of the first occurrence of substring in s.
def find_str(s, substring):
    for i in range(len(s) - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if s[i + j] != substring[j]:
                match = False
                break
        if match:
            return i
    return -1
#Replaces all occurrences of old with new if both are single characters.
def replace_chr(s, old, new):
    if len(old) != 1 or len(new) != 1:
        return ""
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result
#Replaces all occurrences of the string old with new.
def replace_str(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result
