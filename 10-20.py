# Valid paranthesis 

#stack implementation 

def isValid(s):

    x, y, z = "(", "[", "{"
    a,b,c = ")", "]", "}"
    stack = [s[0]]


    for i in range(1, len(s)):
        if(len(stack) == 0):
            stack.append(s[i])
        elif(stack[-1] == x):
            if(s[i] == a):
                stack.pop()
            else:
                stack.append(s[i])
        elif(stack[-1] == y):
            if(s[i] == b):
                stack.pop()
            else:
                stack.append(s[i])
        elif stack[-1] == z:
            if s[i] == c:
                stack.pop()
            else:
                stack.append(s[i])

    return len(stack) == 0
                