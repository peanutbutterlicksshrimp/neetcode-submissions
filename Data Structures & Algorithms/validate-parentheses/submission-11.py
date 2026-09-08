class Solution:
    def find(self, val, s, idx):
        s = s[:idx] + s[idx+1:] #remove the front
        c = 0
        for i in range(idx, len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(": #means we have more open we need to account for
                c+=1
                continue
            elif c > 0: 
                c-=1
                continue
            else:
                if val == "{" and s[i] == "}":
                    s = s[:i] + s[i+1:]
                    return s
                elif val == "(" and s[i] == ")":
                    s = s[:i] + s[i+1:] #remove hte end
                    return s
                elif val == "[" and s[i] == "]":
                    s = s[:i] + s[i+1:]
                    return s

        return s;


    def isValid(self, s: str) -> bool:
        i = 0
        while len(s) > 0:
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                ogS = len(s)
                s = self.find(s[i], s, i)
                if ogS-2 != len(s):
                    return False
            else:
                return False
        return True












        # m = {'{': '}','[': ']','(': ')' }
        # if len(s) % 2 != 0:
        #     return False
        # stack = []
        # for i in range(0, len(s)):
        #     ele = s[i]
        #     if ele in m:
        #         stack.append(ele)
        #     else:
        #         if len(stack) > 0:
        #             p = stack.pop()
        #             match = m.get(p)
        #             if match != s[i]:
        #                 return False
        #         else:
        #             return False
            
        # return True if len(stack) == 0 else False

        
            