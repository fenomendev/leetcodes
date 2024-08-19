def conver(s):
    if s == ')':
        return '('
    if s == ']':
        return '['
    if s == '}':
        return '{'
    return None

def check(s: str):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack[-1] != conver(char):
                return False
            stack.pop()
    return not stack

s = "{[}"
print(check(s))  
