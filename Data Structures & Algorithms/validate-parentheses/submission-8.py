class Solution:
    def isValid(self, s: str) -> bool:
        m = {'{': '}','[': ']','(': ')' }
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(0, len(s)):
            ele = s[i]
            if ele in m:
                stack.append(ele)
            else:
                if len(stack) > 0:
                    p = stack.pop()
                    match = m.get(p)
                    if match != s[i]:
                        return False
                else:
                    return False
            
        return True if len(stack) == 0 else False

        
            