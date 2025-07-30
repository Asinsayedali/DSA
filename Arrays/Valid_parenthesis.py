class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            if paren == '(' or paren == '[' or paren == '{':
                stack.append(paren)
            else:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    if (paren == ')' and top == '(') or (paren == '}' and top == '{' )or( paren == ']' and top == '[') :
                        stack.pop()
                    else:
                        return False
        return not stack
