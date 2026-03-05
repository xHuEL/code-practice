# 对于单字符串而言，一般思路就是遍历整个字符串，然后使用中间变量来维持状态
# 本题思路：找到每个字符左边最近字符的位置a，然后计算当前位置b和左边最近字符的位置a的差值t
# 最后比较每个字符的差值t，找到最大值

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 每个字符的最后出现的位置，位置为str的索引下标。 比如abc，其中字符a的索引位置为-1， b的索引位置为1， c的索引位置为2
        indices_map = {}
        # 最长非重复子串的长度
        max_len = 0
        # 以当前字符为结尾的最长非重复子串的长度
        cur_len = 0

        for index, c in enumerate(s):
            if not indices_map.__contains__(c):
                cur_len = cur_len + 1
            else:
                cur_len = min(index - indices_map[c], cur_len + 1)

            if cur_len > max_len:
                max_len = cur_len
            indices_map[c] = index

        return max_len
