## 最简单的方法是逐个字符串遍历
## 第二种方式：使用二分 + hash
## 第三种方式：trie字典树
import sys
from typing import List


class Solution:
    def find_longest_prefix(self, str1, str2) -> int:
        str_len1 = len(str1)
        str_len2 = len(str2)

        result = 0
        for i in range(min(str_len1, str_len2)):
            if str1[i] != str2[i]:
                break
            result += 1
        return result


    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len = len(strs)
        result = sys.maxsize

        if list_len == 0:
            return strs[0]

        for i in range(list_len):
            result = min(self.find_longest_prefix(strs[0], strs[i]), result)

        return strs[0][0:result]

## trie字典树实现最长公共前缀，参考find-the-length-of-the-longest-common-prefix
## 扩展：如果题目不是最长公共前缀，而是最长匹配子串：（1）两个子串的匹配使用kmp算法 （3）多个子串的匹配使用ac自动机(音乐高亮使用ac自动机,单query匹配多歌词)

