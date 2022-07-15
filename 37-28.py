#  Implement strStr()
# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    
    if len(needle) == 0:
        return 0
    for i in range(len(haystack)):
        
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1