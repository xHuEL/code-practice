class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stk = ['0' for i in range(n)]

        top = 0
        for i in range(n):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stk[top] = s[i]
                top += 1
            else:
                ss = stk[top - 1]
                flag = False
                if s[i] == ']' and ss == '[':
                    flag = True
                elif s[i] == '}' and ss == '{':
                    flag = True
                elif s[i] == ')' and ss == '(':
                    flag = True

                if not flag:
                    return False
                top = top - 1
        if top == 0:
            return True
        return False
