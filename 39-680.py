
# 680. Valid Palindrome II
# Easy

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# approach: This is based on the property that palindromes are same from left and right, so we use two pointers and diverge from the string if we find two elements that do not match even with being at the appropriate locations, then we search without those elements by manipulating pointers ( if s[i] != s[j] then we check the string for i+1 and j OR i and j-1). 

def validPalindrome(s):
    
    i = 0
    j =len(s)-1
    
    while(i < j):
        
        if s[i] != s[j]:
            return isPalindrome(s, i+1, j) or isPalindrome(s, i, j-1)
        i += 1
        j -= 1
        
    return True
                    
                    
def isPalindrome(s, i,j):
    
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
            
    return True


s = "mgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

print(validPalindrome(s))