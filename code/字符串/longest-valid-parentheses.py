## leetcode题目链接：https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=problem-list-v2&envId=string

## 序列的匹配问题：堆栈或者动态规划来实现
## 如果是图的配对问题，一般都是二分匹配或者它的变形

## 这道题：一开始是想着使用堆栈来找到每个）匹配到最长括号长度，比如(())，第一个）匹配到的最长括号为()，第二个）匹配到最长括号为(())，但是遇到这个case ()(())
## 发现最后一个）匹配到的最长括号是(())，但是实际的答案为()(())，所以需要把前面的()长度加上，所以使用一个状态队列来记录每个）匹配到的括号序列的长度。


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ## 堆栈只会压入'('
        stk = [0 for c in s]
        top = 0
        dp = [0 for _ in s]

        ## 当前匹配到的括号的长度
        ans = 0
        for index, c in enumerate(s):
            if c == ')':
                ## 堆栈为空，不压入c
                if top == 0:
                    top = 0
                    continue
                else:
                    match_pos = stk[top - 1]
                    top = top - 1
                    dp[index] = dp[match_pos - 1] + (index - match_pos + 1)
                    if dp[index] > ans:
                        ans = dp[index]
            else:
                stk[top] = index
                top = top + 1
        return ans





