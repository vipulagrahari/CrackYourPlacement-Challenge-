# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string ""

# approach 1: Exhaustive search, complexity O(n^2)
def longestCommonPrefix(strs) -> str:
        
    if len(strs) == 1:
        return strs[0]
    
    
    flag = True
    counter = 0
    res = ""
    while flag:
        
        for i in range(len(strs)):
            
            if len(strs[i]) <= 0:
                return ""
            
            if counter > len(strs[i])-1:
                return res
            
            if strs[i][counter] != strs[0][counter]:
                flag = False
            
        if flag:
            
            res += strs[0][counter]
        counter += 1
    
        return res
