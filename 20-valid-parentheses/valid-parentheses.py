class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            elif bracket in ')}]':
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (bracket == ')' and top == '(') or \
                   (bracket == ']' and top == '[') or \
                   (bracket == '}' and top == '{'):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
